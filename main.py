from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Next.js(3000번 포트)에서 호출할 수 있도록 CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong", "status": "ok"}

@app.post("/api/vod/download")
async def download_vod(payload: dict):
    print("Received payload:", payload)
    video_id = payload.get("video_id")
    start = payload.get("start")
    end = payload.get("end")

    # 여기서 실제 yt-dlp, ffmpeg 같은 로직을 수행 가능
    # 간단한 예시 응답
    return {
        "video_id": video_id,
        "start": start,
        "end": end,
        "status": "download complete"
    }
