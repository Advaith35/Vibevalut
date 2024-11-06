from googleapiclient.discovery import build
import os
import re
API_KEY = "AIzaSyCk4aZ6qvMFA19i4o5r3Hitop-Yj390sKo"  # Replace with your YouTube API key

def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    search_result = youtube.search().list(part="snippet", q=query, maxResults=1).execute()
    if search_result["items"]:
        top_video_id = search_result["items"][0]["id"]["videoId"]
        top_video_url = f"https://www.youtube.com/watch?v={top_video_id}"
        return top_video_url
    else:
        return None

def get_playlist_videos(playlist_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    video_urls = []
    next_page_token = None

    while True:
        playlist_items = youtube.playlistItems().list(
            part="snippet", playlistId=playlist_id, maxResults=50, pageToken=next_page_token
        ).execute()

        # Print out the playlist items to debug
        print("Playlist Items Response:", playlist_items)

        # Loop through the items and get video URLs
        for item in playlist_items["items"]:
            try:
                video_id = item["snippet"]["resourceId"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                video_urls.append(video_url)
                print(f"Added Video URL: {video_url}")
            except KeyError:
                print("Error extracting video ID, skipping item")

        # Check if there are more pages in the playlist
        next_page_token = playlist_items.get("nextPageToken")
        if not next_page_token:
            break

    return video_urls


def is_playlist(input_url):
    # Regex pattern to detect YouTube playlist URLs
    playlist_pattern = r"list=([a-zA-Z0-9_-]+)"
    match = re.search(playlist_pattern, input_url)
    if match:
        return match.group(1)  # Return the playlist ID
    return None

def handle_input(input_url_or_search_term):
    if 'youtube.com/playlist?' in input_url_or_search_term:  # Check for playlist URL
        playlist_id = is_playlist(input_url_or_search_term)
        if playlist_id:
            print(f"Extracting videos from playlist: {input_url_or_search_term}")
            video_links = get_playlist_videos(playlist_id)
            print(f"Video Links Extracted: {video_links}")  # Debugging line
            return video_links
    elif 'youtube.com/watch?' in input_url_or_search_term:  # Check for single video URL
        return [input_url_or_search_term]
    else:
        print(f"Searching YouTube for: {input_url_or_search_term}")
        video_url = search_youtube(input_url_or_search_term)
        if video_url:
            return [video_url]
        return []

if __name__ == "__main__":
    input_term = input("Enter the video URL, playlist URL, or search term: ")
    video_links = handle_input(input_term)
    for link in video_links:
        print(link)
