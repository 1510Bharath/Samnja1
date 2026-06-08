FROM python:3.11-slim
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py questions.py ./
COPY templates/ templates/
COPY static/ static/
RUN mkdir -p uploads
RUN useradd -m samjna && chown -R samjna:samjna /app
USER samjna
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
