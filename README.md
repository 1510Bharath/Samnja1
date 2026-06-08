# Samjna Web — Cloud-Hosted Stress Assessment

## Quick Start (run locally first to test)

```bash
# 1. Install Python 3.11+ if not already installed

# 2. Install dependencies
pip install -r requirements.txt

# 3. Place your avatar image
#    Copy Lady1.jfif into  static/img/Lady1.jfif

# 4. Run the server
python server.py

# 5. Open browser
#    Go to  http://localhost:8000
```

The application will run on port 8000. Participant opens the URL, the entire
interview runs in the browser, and recordings are uploaded to the server.

---

## File Structure

```
samjna_web/
  server.py           ← FastAPI server (all API endpoints)
  questions.py         ← Trilingual question bank + timing config
  requirements.txt     ← Python dependencies
  Dockerfile           ← For cloud deployment
  templates/
    index.html         ← Complete single-page application
  static/
    img/
      Lady1.jfif       ← Avatar image (YOU provide this)
  uploads/             ← Created automatically; recordings saved here
    <Name>_<timestamp>/
      baseline/        ← q1, q2, q3 .webm files
      social_stress/   ← q4, q5, q6 .webm files
      cognitive_stress/← q7, q8, q9 .webm files
      recovery/        ← q10, q11 .webm files
      pss/
        pss_score.csv
      eye_gaze_calibration.csv
      session_log.json
```

---

## Cloud Deployment Options

### Option 1: AWS EC2 (simplest, ~$15-25/month)

1. Launch an EC2 instance (Ubuntu 22.04, t3.small or t3.medium)
2. SSH into the instance
3. Install Docker:
   ```bash
   sudo apt update && sudo apt install -y docker.io docker-compose
   sudo systemctl enable docker
   ```
4. Upload the project:
   ```bash
   scp -r samjna_web/ ubuntu@<your-ec2-ip>:~/
   ```
5. Build and run:
   ```bash
   cd ~/samjna_web
   sudo docker build -t samjna .
   sudo docker run -d -p 80:8000 -v ~/samjna_uploads:/app/uploads --name samjna samjna
   ```
6. Access at  http://<your-ec2-ip>

For HTTPS (required for camera access from non-localhost):
   ```bash
   sudo apt install -y certbot nginx
   # Configure nginx as reverse proxy with SSL
   ```

### Option 2: Google Cloud Run (auto-scaling, pay-per-use)

1. Install Google Cloud CLI: https://cloud.google.com/sdk/docs/install
2. Build and deploy:
   ```bash
   gcloud builds submit --tag gcr.io/<PROJECT_ID>/samjna
   gcloud run deploy samjna --image gcr.io/<PROJECT_ID>/samjna \
     --platform managed --region asia-south1 --allow-unauthenticated
   ```
3. Access at the URL provided by Cloud Run

Note: Cloud Run is stateless — uploads need to be saved to Google Cloud
Storage instead of local disk. Modify server.py accordingly.

### Option 3: Railway / Render (easiest, free tier available)

1. Push code to a GitHub repository
2. Go to https://railway.app or https://render.com
3. Connect your GitHub repo
4. It auto-detects the Dockerfile and deploys
5. Access at the provided URL

---

## Important: HTTPS Required

Modern browsers require HTTPS to access the camera and microphone.
On localhost this works without HTTPS, but on a public URL you MUST
have HTTPS enabled. All cloud platforms above support HTTPS.

---

## Timing Configuration

Edit these values in `questions.py` → `PHASES` list:

| Phase            | Response time (q_secs) | Prep time (prep_secs) |
|------------------|------------------------|-----------------------|
| Baseline         | 25                     | 2                     |
| Social Stress    | 25                     | 15                    |
| Cognitive Stress | 25                     | 5                     |
| Recovery         | 60                     | 1                     |

---

## Recording Format

Browser MediaRecorder produces `.webm` files (VP8 video + Opus audio).
These are fully compatible with ffmpeg, VLC, and your analysis pipeline.

To convert to MP4 after download (if needed):
```bash
ffmpeg -i recording.webm -c:v libx264 -c:a aac output.mp4
```

To extract audio as WAV for analysis:
```bash
ffmpeg -i recording.webm -vn -acodec pcm_s16le -ar 16000 -ac 1 output.wav
```
