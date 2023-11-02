from pydub import AudioSegment
import eyed3
import subprocess
import os

def m4a_to_mp3(file_name):
	m4a_file = AudioSegment.from_file(file_name, format="m4a")
		
	m4a_file.export(f"{file_name[:-4]}.mp3", format="mp3")

def add_metadata(file_name, artist, title, album = None):

	mp3_file = eyed3.load(file_name)
	mp3_file.tag.artist = artist
	mp3_file.tag.title = title

	if album is not None:
		mp3_file.tag.album = album
	
	mp3_file.tag.save()

def fix_file(file_name, directory, silence_log = True):
	
	if silence_log:
		subprocess.run(["ffmpeg","-loglevel","quiet", "-i", file_name, "-acodec", "copy", f"{directory}/file_fixed.mp3"])
	else:
		subprocess.run(["ffmpeg","-i", file_name, "-acodec", "copy", f"{directory}/file_fixed.mp3"])

	os.remove(file_name)
	os.rename(f"{directory}/file_fixed.mp3", file_name),
