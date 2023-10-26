from pydub import AudioSegment


def m4a_to_mp3(file_name,  meta_data = None):
	m4a_file = AudioSegment.from_file(file_name, format="m4a")
		
	m4a_file.export(f"{file_name[:-4]}.mp3", format="mp3")
		
