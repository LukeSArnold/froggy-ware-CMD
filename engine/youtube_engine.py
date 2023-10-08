from pytube import YouTube 
import os 
from youtubesearchpython import VideosSearch

class YoutubeEngine:
	def __init__(self, log_bool = False):
		self.logging = log_bool
	
	def search_from_list(self, songs, lyrics_correction = False):
		song_info = []
		for song in songs:
			#assuming list of songs is passed in from spotify_engine
			artist = song['artist']
			track = song['track']
			searchString = "{} {} ".format(track,artist)	
			videosSearch = VideosSearch(searchString, limit = 2)
			title = ((((videosSearch.result())['result'])[0])['title']).lower()

			if self.logging:
				print(title)

			#check to see if video is in title, trying to filter out music videos
			if "video" not in title:
				link = (((videosSearch.result())['result'])[0])['link']

			else:
				if lyrics_correction:
					searchString = "{} {} {}".format(track,artist,"lyrics")
					videosSearch = VideosSearch(searchString, limit = 1)
					alternate_song = (((videosSearch.result())['result'])[0])['title'].lower()					

					if self.logging:
						print(f"{title} was a music video, because lyrics is enable, using {alternate_song} instead")

					link = (((videosSearch.result())['result'])[0])['link']
				else:
					alternate_song = (((videosSearch.result())['result'])[1])['title'].lower()

					if track.lower() in alternate_song:

					
						#check to see if the song name itself has video in the name
						if "video" not in track.lower():
							#music video filtered, take second youtube results
						
							if self.logging:
								print(f"{title} was a music video, using {alternate_song} instead")
						
							link = (((videosSearch.result())['result'])[1])['link']		

						elif "music video" not in title:
							#"video" included in song name, check to see if it is also a youtube video
							link = (((videosSearch.result())['result'])[0])['link']

						else:
							#video is included in track name, and first result is a music video. Filter

							if self.logging:
								print(f"{title} was a music video, using {alternate_song} instead")
							link = (((videosSearch.result())['result'])[1])['link']

					else:
						if self.logging:
							print(f"The search {title} is possibly a music video, but the second result {alternate_song} wasn't the same song. Converting the first link and taking chances")

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
