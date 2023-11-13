from engine.froggy_engine import FroggyEngine
import time
import os
import sys

if __name__ == "__main__":


	# if -a add album art
	# if -v verbose meta data
	# if -l add logging
	# if --sam add sam configuration

	arguments = sys.argv

	# checking cmd arguments
	album_art = False
	verbose_data = False
	logging = False
	sam_config = False

	if "-a" in arguments:
		album_art = True

	if "-v" in arguments:
		verbose_data = True

	if "-l" in arguments:
		logging = True

	if "--sam" in arguments:
		sam_config = True
	
	playlist_url = input("INPUT URL\n:")
	playlist_name = input("INPUT PLAYLIST NAME\n:")
        
	desktop_path = os.path.expanduser("~/Desktop")
	directory = ""+desktop_path+"/"+playlist_name

	engine = FroggyEngine(playlist_url, directory, verbose_data, album_art, logging, sam_config)

	engine.convert()

	sys.exit(1)
