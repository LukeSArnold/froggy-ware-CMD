from  engine. spotify_engine import SpotifyEngine
#from  engine.youtube_engine import YoutubeEngine
from engine.youtube_engine_2 import YoutubeEngine
import threading
import time
import os
import sys

class FroggyEngine:
	def __init__(self, url, directory, verbose_metadata = False, album_art = False, logging = False, is_album = False, SAM_configuration = False, no_persist = False):
		
		url = url
		self.directory = directory
		self.spotify_engine = SpotifyEngine(url)
		self.youtube_engine = YoutubeEngine(logging)

		self.logging = logging
		self.verbose_metadata = verbose_metadata
		self.SAM_configuration = SAM_configuration
		self.is_album = is_album
		self.no_persist = no_persist


	def convert(self):
		start = time.time()

		os.mkdir(self.directory)

		if self.is_album:
			songs = self.spotify_engine.get_album(self.verbose_metadata)
		else:
			songs = self.spotify_engine.get_playlists(self.verbose_metadata)
		
		if self.logging:
			print("...SPOTIFY INFO SECURED")

		youtube_links = self.youtube_engine.search_from_list(songs)

		if self.logging:
			print("...YOUTUBE LINKS CONVERTED")

		if not self.no_persist:
			if self.verbose_metadata:
				for song in youtube_links:
					self.youtube_engine.download_track(song['link'], song['artist'], song['track'], self.directory, self.SAM_configuration, song)

			else:
				for song in youtube_links:
					self.youtube_engine.download_track(song['link'], song['artist'], song['track'], self.directory, self.SAM_configuration)


			if self.logging:
				print("YOUR SONGS ARE READY")
				print("CONVERTED {} SONGS IN {} SECONDS".format((len(youtube_links)),(time.time() - start)))

		else:
			print("NOT CONVERTING SONGS, NO PERSIST IN CONFIGURATION")	

			
