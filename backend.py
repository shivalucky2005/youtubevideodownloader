import os
from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
import yt_dlp # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific frontend domains in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get current working directory
cur_dir = os.getcwd()

# Define the request model
class DownloadRequest(BaseModel):
    link: str

@app.post("/download")
async def download_video(request: DownloadRequest):
    # Ensure the current working directory exists
    os.makedirs(cur_dir, exist_ok=True)

    # Generate a unique filename
    video_filename = "ABCsample.mp4"  # Adjust this to generate unique filenames dynamically if required

    # Define yt-dlp options
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, video_filename),
    }

    try:
        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([request.link])

        return {
            "status": "success",
            "message": "Video downloaded successfully!",
            "file_name": video_filename,
        }
    except Exception as e:
        # Raise HTTPException for any errors
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")
