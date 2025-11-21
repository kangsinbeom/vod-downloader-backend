import subprocess
import os
import aiohttp
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"],
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

@app.post("/api/vod/download")
async def download_vod(payload: dict):
    print("Received payload:", payload)
    
    # Step 1: 클라이언트로부터 받은 데이터
    segment_urls = payload.get("segmentUrls")  # TS 파일 URL 배열
    output_filename = payload.get("output_filename", "output.mp4")

    # Step 2: segment URL 목록을 input.txt 파일로 저장
    with open("input.txt", "w") as f:
        for url in segment_urls:
            f.write(f"file '{url}'\n")

    # Step 3: ffmpeg로 병합 실행
    ffmpeg_cmd = [
        "ffmpeg",
        "-protocol_whitelist", "file,http,https,tcp,tls",
        "-f", "concat",
        "-safe", "0",
        "-i", "input.txt",
        "-c", "copy",
        output_filename,
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        return {
            "status": "success",
            "output_file": output_filename,
            "message": "Video merged successfully."
        }
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

