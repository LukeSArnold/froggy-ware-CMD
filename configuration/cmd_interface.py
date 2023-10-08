from spotify_engine import SpotifyEngine
from youtube_engine import YoutubeEngine
import threading
import time
import os
import sys

if __name__ == "__main__":


	playlist_url = input("INPUT URL\n:")

	engine = SpotifyEngine(playlist_url)
	youtube_engine = YoutubeEngine(True)
        
	#making folder on desktop
	playlist_name = input("name directory\n:")
	
	
	start = time.time()

	desktop_path = os.path.expanduser("~/Desktop")

	directory = ""+desktop_path+"/"+playlist_name
	os.mkdir(directory)

	songs = engine.get_playlists()
	print("...SPOTIFY INFO SECURED")

	youtube_links = youtube_engine.search_from_list(songs)
	print("...YOUTUBE LINKS CONVERTED")
	
	for song in youtube_links:
		youtube_engine.download_track(song['link'], song['artist'], song['track'], directory)

	print("YOUR SONGS ARE READY")
	
	print("CONVERTED {} SONGS IN {} SECONDS".format((len(youtube_links)),(time.time() - start)))

	sys.exit(1)
