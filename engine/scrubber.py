from pydub import AudioSegment

class Scrubber:
	def __init__(self, file_name):
		self.file_name = file_name

	def convert(self):
		m4a_file = AudioSegment.from_file(self.file_name, format="m4a")
		
		m4a_file.export("audio.mp3", format="mp3")
		
