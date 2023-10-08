import dearpygui.dearpygui as dpg
from engine.spotify_engine import SpotifyEngine
from engine.youtube_engine import YoutubeEngine
import threading
import time
import os
import sys
import random



#try:

dpg.create_context()

def callback(sender, app_data):
	print('OK was clicked.')
	print("Sender: ", sender)
	print("App Data: ", app_data)
	dpg.set_value(folder, app_data['file_path_name'])
	
def cancel_callback(sender, app_data):
	print('Cancel was clicked.')
	print("Sender: ", sender)
	print("App Data: ", app_data)

def reset(sender, app_data):
	desktop_path = os.path.expanduser("~/Desktop")
	dpg.set_value(folder, desktop_path+ "/MyPlaylist")

def convert(sender, app_data):

	try:	
		dpg.set_value(status_string, "...RUNNING")

		playlist_url = dpg.get_value(spotify_url) 
		engine = SpotifyEngine(playlist_url)
		youtube_engine = YoutubeEngine()

		directory = dpg.get_value(folder)

		dpg.set_value(status_string, "...GETTING SPOTIFY SONGS")
		songs = engine.get_playlists()
		dpg.set_value(status_string, "...SONGS ACQUIRED")

		dpg.set_value(status_string, "...FINDING SONGS ON YOUTUBE")

		youtube_links = youtube_engine.search_from_list(songs, True)


		dpg.set_value(status_string, "...CONVERTING SONGS")


		if os.path.exists(directory):
			directory = directory + (str(time.asctime())).replace(" ","_")
			os.mkdir(directory)
		else:
			os.mkdir(directory)
		
		for song in youtube_links:
			youtube_engine.download_track(song['link'], song['artist'], song['track'], directory)
			dpg.set_value(status_string, "...CONVERTED {} BY {}".format(song['track'],song['artist']))

		dpg.set_value(status_string, "All Done!")
		time.sleep(2)
		dpg.set_value(status_string, "")
	except Exception as error:
		print(error)
		dpg.set_value(status_string, "Something went wrong, is your playlist public?")

with dpg.window(tag="Primary Window"):
	dpg.add_text("Luke's Spotify Converter")
	spotify_url = dpg.add_input_text(label="Spotify Playlsit URL")
	desktop_path = os.path.expanduser("~/Desktop")
	folder = dpg.add_input_text(label="Folder to save", default_value=desktop_path+"/MyPlaylist")
	status_string = dpg.add_input_text(label="STATUS", default_value="")
	dpg.add_button(label="CONVERT", callback = convert)
	dpg.add_file_dialog(
		directory_selector=True, show=False, callback=callback, tag="file_dialog_id",
		cancel_callback=cancel_callback, width=700 ,height=400)
	
	dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file_dialog_id"))
	dpg.add_button(label="Reset Directory", callback = reset)
dpg.create_viewport(title="Lukey's Spotify Converter", width=800, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
#except Exception as error:
#	print("An error occured: "+error)
