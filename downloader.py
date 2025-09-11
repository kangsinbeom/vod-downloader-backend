import ffmpeg
import os

def download_video(url: str, output_name: str):
    """
    URL에서 전체 동영상을 ffmpeg로 다운로드
    """
    output_path = os.path.join("videos", output_name)
    if not os.path.exists("videos"):
        os.makedirs("videos")

    try:
        # 전체 다운로드는 start_time, end_time 없이 입력
        (
            ffmpeg
            .input(url)
            .output(output_path, c='copy')
            .run(overwrite_output=True)
        )
        return output_path
    except ffmpeg.Error as e:
        return f"FFmpeg error: {e}"