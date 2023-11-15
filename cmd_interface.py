from engine.froggy_engine import FroggyEngine
import time
import os
import sys


try:
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
		is_album = False
		sam_config = False
		no_persist = False


		if "-c" in arguments:
			album_art = True

		if "-v" in arguments:
			verbose_data = True

		if "-l" in arguments:
			logging = True

		if "-a" in arguments:
			is_album = True

		if "--sam" in arguments:
			sam_config = True

		if "--no-persist" in arguments:
                        no_persist = True
		
		content_url = input("INPUT URL\n:")
		playlist_name = input("INPUT PLAYLIST NAME\n:")
		
		desktop_path = os.path.expanduser("~/Desktop")
		directory = ""+desktop_path+"/"+playlist_name

		engine = FroggyEngine(content_url, directory, verbose_data, album_art, logging, is_album, sam_config, no_persist)

		engine.convert()

		sys.exit(1)
except KeyboardInterrupt:
	print("...TERMINATING...")
	sys.exit(1)
