from pytube import YouTube 
import os 
from youtubesearchpython import VideosSearch

class YoutubeEngine:
	def __init__(self, log_bool = False):
		self.logging = log_bool
	
	def search_from_list(self, songs):
		song_info = []
		for song in songs:
			#assuming list of songs is passed in from spotify_engine
			artist = song['artist']
			track = song['track']

			searchString = "{} {} lyrics".format(track,artist)	
			videosSearch = VideosSearch(searchString, limit = 1)
			link = (((videosSearch.result())['result'])[0])['link']
			
			track = {'link':link, 'artist':artist, 'track':track}
			song_info.append(track)
			
		return song_info

			

	def download_track(self, url, artist, track, directory):
		yt = YouTube(url,use_oauth=True,allow_oauth_cache=True)
		video = yt.streams.filter(only_audio=True).first()

		destination = "../exports"
  
		# download the file 
		out_file = video.download(output_path=directory) 
		base, ext = os.path.splitext(directory+"/"+out_file) 
		new_file = "" + track + "_" + artist + '.mp3'
		new_file = new_file.replace(" ","_")
		os.rename(out_file, directory+"/"+new_file)  

		if self.logging:
			print("...CONVERTED {}".format(new_file))
