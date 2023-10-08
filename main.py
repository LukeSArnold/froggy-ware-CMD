import dearpygui.dearpygui as dpg
from spotify_engine import SpotifyEngine
from youtube_engine import YoutubeEngine
import threading
import time
import os
import sys

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
	playlist_url = dpg.get_value(spotify_url) 
	engine = SpotifyEngine(playlist_url)
	youtube_engine = YoutubeEngine()

	directory = dpg.get_value(folder)
	os.mkdir(directory)

	songs = engine.get_playlists()
	youtube_links = youtube_engine.search_from_list(songs)
	
	for song in youtube_links:
		youtube_engine.download_track(song['link'], song['artist'], song['track'], directory)

	
	
	


dpg.create_context()

with dpg.window(tag="Primary Window"):
	dpg.add_text("Luke's Spotify Converter")
	spotify_url = dpg.add_input_text(label="Spotify Playlsit URL")

	desktop_path = os.path.expanduser("~/Desktop")
	folder = dpg.add_input_text(label="Folder to save", default_value=desktop_path+"/MyPlaylist")
	dpg.add_button(label="CONVERT", callback = convert)
	dpg.add_file_dialog(
		directory_selector=True, show=False, callback=callback, tag="file_dialog_id",
   		cancel_callback=cancel_callback, width=700 ,height=400)
	
	dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file_dialog_id"))
	dpg.add_button(label="Reset Directory", callback = reset)

dpg.create_viewport(title="Lukey's Spotify Converter", width=1500, height=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
