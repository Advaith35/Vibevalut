from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os

def download_audio(video_url, output_path="."):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save in specified output path
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the URL of the video you want to download: ")
    output_path = input("Enter the destination (leave blank for current directory): ") or "."
    download_audio(video_url, output_path)
