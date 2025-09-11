from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from downloader import download_video
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VOD Downloader API")

class DownloadRequest(BaseModel):
    url: str
    output_name: str

@app.post("/download")
def download_vod(req: DownloadRequest):
    result = download_video(req.url, req.output_name)
    if "FFmpeg error" in result:
        raise HTTPException(status_code=500, detail=result)
    return {"message": "Download completed", "file": result}

# 허용할 Origin 설정
origins = [
    "http://localhost:3000",   # Next.js 개발 서버
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
