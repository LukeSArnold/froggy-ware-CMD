# froggy_ware

Froggy Ware is a spotify to mp3 converter. As it stands now, Froggy Ware is only capable of converting public spotify playlists to mp3. The current version of Froggy Ware is only for MacOS, though future releases plan to cover Windows and Linux based machines. 

## DEPENDENCIES

Froggy Ware handles most install and setup of necessary python libraries and the FFMPEG tool. These can be simply setup in the built in `setup.py` file, **see "SETUP"**. Though, the setup.py file is setup for mac users and requires that *Homebrew* must be installed on your computer to install the necessary depencies. For MacOS, simply run the command `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` to install Homebrew. If using Linux or Windows FFmpeg must be independently installed on your machine. 

## SETUP

After running 
```git clone https://github.com/LukeSArnold/froggy_ware```

Simply navigate to `/configuration/` and run `setup.py`. This file will pip3 install all necessary dependencies to run froggy_ware.

It is important to first run Froggy Ware with a terminal open, as the system may require you to follow a link and provide google authentitaiton. This is because Froggy Ware automates the YouTube to mp3 conversion process, and occassionally pulls age protected content during the conversin process. Therefore, Froggy Ware occasionally requires google authenticaion to pull this content. This authentication is completely isolated to your own Google account and local computer. 

Google authentication will only be required once, and will continue to run on the same google account.
`
## USE

Froggy Ware can be accessed through either a command line interface. Simply run `cmd_interface.py`. 
The CMD line can take in a series of configuration values which will all correspond to specific functionality for either use or testing. 


the `-l` tag will enable logging, providing continual updates to the programs execution


the `-v` tag will enable verbose metadata configuration, implenting release date information, album track listing, but most notably, it adds **album artwork** to the mp3 files


the `-a` tag will allow Froggy Ware to convert albums from spotify, if this tag is not included an error will be thrown when converting an album. 


the `--sam` tag will format final mp3s with an `artist - track.mp3` format, which differs from the standard `track_artist.mp3` convention


the `--no-persist` tag will fetch the information from spotify, but will not convert the mp3s. 
