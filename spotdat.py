import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re

# Replace with your own credentials
client_id = 'f67f196a44d64ae68b0da778bbba78f9'
client_secret = 'd6b0ff24e6434b67a2fe9c2f37d18404'
redirect_uri = 'http://localhost:3000'  # Must match your Spotify Developer Dashboard

# Initialize the Spotify client with necessary permissions
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-read-private"))

# Function to extract playlist ID from a Spotify link
def extract_playlist_id(playlist_link):
    regex = r"playlist/([a-zA-Z0-9]+)"
    match = re.search(regex, playlist_link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid playlist link.")

# Function to get playlist name and tracks in the required format
def get_playlist_tracks(playlist_link):
    try:
        playlist_id = extract_playlist_id(playlist_link)
        playlist = sp.playlist(playlist_id)  # Fetch playlist details
        playlist_name = playlist['name']  # Get the playlist name
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']

        # Retrieve all track names hyphenated with artist names
        track_list = [playlist_name]  # Initialize with the playlist name
        for item in tracks:
            track = item['track']
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_list.append(f"{track_name} - {artist_name}")
        
        return track_list

    except Exception as e:
        return str(e)

# Remove or comment out the following block to prevent double input request
# if __name__ == "__main__":
#    playlist_link = input("Enter the Spotify playlist link: ")
#    tracks = get_playlist_tracks(playlist_link)
#    
#    for track in tracks:
#        print(track)
