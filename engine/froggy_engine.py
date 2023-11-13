from  engine. spotify_engine import SpotifyEngine
from  engine.youtube_engine import YoutubeEngine
import threading
import time
import os
import sys

class FroggyEngine:
	def __init__(self, url, directory, verbose_metadata = False, album_art = False, logging = False, SAM_configuration = False):
		
		url = url
		self.directory = directory
		self.spotify_engine = SpotifyEngine(url)
		self.youtube_engine = YoutubeEngine(logging)

		self.logging = logging
		self.verbose_metadata = verbose_metadata
		self.SAM_configuration = SAM_configuration


	def convert(self):
		start = time.time()

		os.mkdir(self.directory)

		songs = self.spotify_engine.get_playlists(self.verbose_metadata)
		
		if self.logging:
			print("...SPOTIFY INFO SECURED")

		youtube_links = self.youtube_engine.search_from_list(songs)

		if self.logging:
			print("...YOUTUBE LINKS CONVERTED")

		if self.verbose_metadata:
			for song in youtube_links:
				self.youtube_engine.download_track(song['link'], song['artist'], song['track'], self.directory, self.SAM_configuration, song)

		else:
			for song in youtube_links:
                                self.youtube_engine.download_track(song['link'], song['artist'], song['track'], self.directory, self.SAM_configuration)


		if self.logging:
			print("YOUR SONGS ARE READY")
			print("CONVERTED {} SONGS IN {} SECONDS".format((len(youtube_links)),(time.time() - start)))

		

		