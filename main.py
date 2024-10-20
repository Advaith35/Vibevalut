import re
from ytinfo import search_youtube
from m3downloader import download_audio
from spotdat import get_playlist_tracks  # Import the Spotify function
import os

def is_spotify_link(link):
    # Regex to check if the input link is a Spotify playlist link
    return re.search(r"open.spotify.com/playlist/", link) is not None

def main():
    link = input("Enter the YouTube or Spotify playlist link: ")

    if is_spotify_link(link):
        print(f"Fetching Spotify playlist details for: {link}")
        tracks = get_playlist_tracks(link)
        
        if isinstance(tracks, list) and len(tracks) > 0:
            playlist_name = tracks[0]  # First element is the playlist name

            # Create a folder for the playlist in the Music directory
            music_folder = os.path.join(os.path.expanduser('~'), 'Music', playlist_name)
            if not os.path.exists(music_folder):
                os.makedirs(music_folder)

            print(f"Created folder: {music_folder}")
            
            # Loop through tracks and download each from YouTube
            for track in tracks[1:]:  # Skip the playlist name
                print(f"Searching and downloading: {track}")
                video_url = search_youtube(track)
                if video_url:
                    print(f"Found YouTube video: {video_url}")
                    download_audio(video_url, music_folder)
                else:
                    print(f"Could not find YouTube video for track: {track}")
        else:
            print("No tracks found or an error occurred.")

    else:
        print(f"Searching YouTube for: {link}")
        video_url = search_youtube(link)
        
        if video_url:
            print(f"Found video: {video_url}")
            output_path = os.path.join(os.path.expanduser('~'), 'Music')
            download_audio(video_url, output_path)
        else:
            print("No video found for the given link.")

if __name__ == "__main__":
    main()
