from pydub import AudioSegment
import eyed3

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
