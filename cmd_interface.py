from engine.froggy_engine import FroggyEngine
import threading
import time
import os
import sys

if __name__ == "__main__":


	playlist_url = input("INPUT URL\n:")
	playlist_name = input("INPUT PLAYLIST NAME\n:")
        
	desktop_path = os.path.expanduser("~/Desktop")
	directory = ""+desktop_path+"/"+playlist_name

	engine = FroggyEngine(playlist_url, directory, True, True)

	engine.convert()

	sys.exit(1)
