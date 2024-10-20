# VibeVault

**VibeVault** is an innovative audio downloader that allows you to effortlessly collect your favorite tracks from various sources. Whether you have a song title, a YouTube video link, or a playlist from Spotify or YouTube, VibeVault retrieves and downloads your desired audio in high-quality MP3 format to your local device.

## Features

- **Multi-source support:** Download songs from YouTube videos and Spotify playlists.
- **High-quality audio:** Downloads tracks in MP3 format.
- **User-friendly interface:** Simple input prompts for easy interaction.
- **Automatic folder creation:** Organizes downloaded playlists in your Music directory.

## Requirements

- Python 3.x
- Required libraries:
  - `yt-dlp`
  - `spotipy`
  - `google-api-python-client`
  
## Installation

1. **Clone the repository:**
   ```bash
   git clone <[repository-url](https://github.com/Advaith35/Vibevalut)>
   cd VibeVault
2. **Install the required libraries:**
   ```bash
   pip install yt-dlp spotipy google-api-python-client
3. **Set up API keys:**
   - Replace `API_KEY_enter` in `ytinfo.py` with your YouTube API key.
   - Replace `Client_id_enter`, `Client_secret_enter`, and `redirect_uri` in `spotdat.py` with your Spotify Developer credentials.

## Usage

1. Run the main program:
   ```bash
   python main.py
2. **Enter a YouTube video link, Spotify playlist link, or search term when prompted.**
3. **If a Spotify playlist link is provided, VibeVault will create a folder named after the playlist in your Music directory and download each track from YouTube.**

4. **If a YouTube video link is provided, it will download the audio directly to your Music directory.**

## Example

To download a Spotify playlist:
   ```bash

    Enter the YouTube or Spotify playlist link: open.spotify.com/playlist/your_playlist_id

```

that's it if you enter the link it will automatically do the rest . 

Thank You 
Hope you use it well !




