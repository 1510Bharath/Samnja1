# =============================================================================
# server.py — Samjna Web Server (FastAPI)
#
# Endpoints:
#   GET  /                    → Serve the single-page application
#   POST /api/session         → Create session (returns session_id + questions)
#   POST /api/upload/{sid}/{qid}  → Upload video+audio for one question
#   POST /api/gaze/{sid}      → Upload eye gaze CSV data
#   POST /api/pss/{sid}       → Submit PSS answers, get score
#   GET  /api/avatar          → Serve the avatar image
# =============================================================================

import os
import json
import csv
import uuid
import datetime
import logging
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from questions import build_session, PSS, PSS_OPTIONS, PSS_REVERSED, PHASES

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("samjna")

app = FastAPI(title="Samjna Stress Assessment")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent
# Output folder — same location as the desktop app
UPLOAD_DIR  = UPLOAD_DIR = BASE_DIR / "Output"
STATIC_DIR  = BASE_DIR / "static"
TEMPLATE_DIR = BASE_DIR / "templates"
AVATAR_PATH = BASE_DIR / "static" / "img" / "Lady1.jfif"

UPLOAD_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)
(STATIC_DIR / "img").mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# In-memory session store (use Redis/DB in production)
sessions: dict = {}


# ── Serve the SPA ─────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = TEMPLATE_DIR / "index.html"
    with open(html_path, encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# ── Create session ────────────────────────────────────────────────────────────

@app.post("/api/session")
async def create_session(name: str = Form(...), language: str = Form("english")):
    sid = uuid.uuid4().hex[:12]
    ts  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() else "_" for c in name).strip("_")
    folder_name = f"{safe_name}_{ts}"

    session_dir = UPLOAD_DIR / folder_name
    for sub in ("baseline", "social_stress", "cognitive_stress", "recovery", "pss"):
        (session_dir / sub).mkdir(parents=True, exist_ok=True)

    interview = build_session(language)

    sessions[sid] = {
        "name":       name,
        "safe_name":  safe_name,
        "language":   language,
        "timestamp":  ts,
        "dir":        str(session_dir),
        "interview":  interview,
        "events":     [],
    }

    log.info("Session created: %s (%s, %s)", sid, name, language)

    return {
        "session_id": sid,
        "interview":  interview,
        "pss": {
            "questions": PSS.get(language, PSS["english"]),
            "options":   PSS_OPTIONS.get(language, PSS_OPTIONS["english"]),
        },
        "phases": PHASES,
    }


# ── Upload recording ──────────────────────────────────────────────────────────

@app.post("/api/upload/{sid}/{qid}")
async def upload_recording(
    sid: str,
    qid: str,
    video: UploadFile = File(None),
    audio: UploadFile = File(None),
):
    sess = sessions.get(sid)
    if not sess:
        return JSONResponse({"error": "Invalid session"}, status_code=404)

    # Determine phase subfolder from qid (q1-q3=baseline, q4-q6=social, etc.)
    q_num = int(qid.lstrip("q"))
    if q_num <= 3:
        phase = "baseline"
    elif q_num <= 6:
        phase = "social_stress"
    elif q_num <= 9:
        phase = "cognitive_stress"
    else:
        phase = "recovery"

    phase_dir = Path(sess["dir"]) / phase
    base = f"{sess['safe_name']}_{qid}_{sess['timestamp']}"

    saved = []
    if video:
        vpath = phase_dir / f"{base}.webm"
        with open(vpath, "wb") as f:
            f.write(await video.read())
        saved.append(str(vpath))
        log.info("  Video saved: %s (%.1f KB)", vpath.name, vpath.stat().st_size / 1024)

    if audio:
        apath = phase_dir / f"{base}.wav"
        with open(apath, "wb") as f:
            f.write(await audio.read())
        saved.append(str(apath))
        log.info("  Audio saved: %s (%.1f KB)", apath.name, apath.stat().st_size / 1024)

    sess["events"].append({
        "time": datetime.datetime.now().isoformat(),
        "event": f"UPLOAD_{qid}",
        "files": saved,
    })

    return {"status": "ok", "files": saved}


# ── Eye gaze data ─────────────────────────────────────────────────────────────

@app.post("/api/gaze/{sid}")
async def save_gaze(sid: str, request: Request):
    sess = sessions.get(sid)
    if not sess:
        return JSONResponse({"error": "Invalid session"}, status_code=404)

    data = await request.json()
    gaze_path = Path(sess["dir"]) / "eye_gaze_calibration.csv"

    with open(gaze_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["dot_index", "target_x", "target_y",
                                                "click_x", "click_y", "offset", "timestamp"])
        writer.writeheader()
        writer.writerows(data.get("dots", []))

    log.info("  Gaze CSV saved: %s", gaze_path.name)
    return {"status": "ok"}


# ── PSS submission ────────────────────────────────────────────────────────────

@app.post("/api/pss/{sid}")
async def submit_pss(sid: str, request: Request):
    sess = sessions.get(sid)
    if not sess:
        return JSONResponse({"error": "Invalid session"}, status_code=404)

    data = await request.json()
    answers = data.get("answers", [])

    # Score with reverse coding
    scored = []
    for i, val in enumerate(answers):
        scored.append(4 - val if i in PSS_REVERSED else val)
    total = sum(scored)

    if total <= 13:
        interp = "Low perceived stress (0–13)"
    elif total <= 26:
        interp = "Moderate perceived stress (14–26)"
    else:
        interp = "High perceived stress (27–40)"

    # Save CSV
    pss_path = Path(sess["dir"]) / "pss" / "pss_score.csv"
    with open(pss_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Question_No", "Answer_Value"])
        for i, v in enumerate(answers, 1):
            w.writerow([i, v])
        w.writerow([])
        w.writerow(["Total_PSS_Score", total])
        w.writerow(["Interpretation", interp])
        w.writerow([])
        w.writerow(["participant_name", "pss_score"])
        w.writerow([sess["name"], total])

    # Save session log
    sess["events"].append({"time": datetime.datetime.now().isoformat(),
                           "event": "PSS_COMPLETE", "score": total})
    log_path = Path(sess["dir"]) / "session_log.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({"participant": sess["name"], "language": sess["language"],
                    "timestamp": sess["timestamp"], "events": sess["events"]}, f, indent=2)

    log.info("  PSS score: %d (%s)", total, interp)
    return {
        "score":         total,
        "interpretation": interp,
        "output_folder": str(Path(sess["dir"])),
    }


# ── Avatar image ──────────────────────────────────────────────────────────────

@app.get("/api/avatar")
async def get_avatar():
    # Try multiple extensions
    for ext in (".jfif", ".jpg", ".jpeg", ".png"):
        p = STATIC_DIR / "img" / f"Lady1{ext}"
        if p.exists():
            return FileResponse(str(p))
    return JSONResponse({"error": "Avatar not found"}, status_code=404)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
