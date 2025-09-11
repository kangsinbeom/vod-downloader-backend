import requests
import ffmpeg
import json
import os

# 설정 로드
with open("config/config.json", "r") as f:
    config = json.load(f)
cookies = config.get("cookies", {})

# 테스트용 스트림 URL (실제 VOD에서는 DASH/MP4 URL 필요)
stream_url = 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'


output_path = "output.mp4"

print("Downloading...")

(
    ffmpeg
    .input(stream_url)
    .output(output_path, c='copy')
    .run()
)

print(f"Download completed: {os.path.abspath(output_path)}")
