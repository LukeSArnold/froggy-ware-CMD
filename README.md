# froggy_ware

Froggy Ware is a spotify to mp3 converter. As it stands now, Froggy Ware is only capable of converting public spotify playlists to mp3. The current version of Froggy Ware is only for MacOS, though future releases plan to cover Windows and Linux based machines. 

## DEPENDENCIES

Froggy Ware handles most install and setup of necessary python libraries and the FFMPEG tool. These can be simply setup in the built in `setup.py` file, **see "SETUP"**. Though, *Homebrew* must be installed on your computer to install the necessary depencies. For MacOS, simply run the command `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` to install Homebrew. 

## SETUP

After running 
```git clone https://github.com/LukeSArnold/froggy_ware```

Simply navigate to `/configuration/` and run `setup.py`. This file will pip3 install all necessary dependencies to run froggy_ware.

It is important to first run Froggy Ware with a terminal open, as the system may require you to follow a link and provide google authentitaiton. This is because Froggy Ware automates the YouTube to mp3 conversion process, and occassionally pulls age protected content during the conversin process. Therefore, Froggy Ware occasionally requires google authenticaion to pull this content. This authentication is completely isolated to your own Google account and local computer. 

Google authentication will only be required once, and will continue to run on the same google account.
`
## USE

Froggy Ware can be accessed through either a command line interface, or through the built in graphical user interface. Simply run `cmd_interface.py` for the CMD line, or `main.py` for the GUI. 

### GUI

The GUI contains a few distinct fields,

    1.   the "Spotify Playlist URL" input, simply copy and paste the URL for your Spotify playlist here. To get this URL Spotify must be accessed through browser, as desktop application spoitfy doesn't contain any URLs

    2.   the "Folder to save' input. Froggy Ware defaults to saving to Desktop under the general directory name "MyPlaylist". This path can be changed to specify different directories to save to. If a directory doesn't already exist, Froggy Ware will create the directory. This folder can also be chosen by clicking the "Directory Selector" button at the bottom of the page.

    3.   "Status" input. This exist to provide the status of the program while converting. Any text entered into this input will be ignored and wiped during execution.

    4.   "Convert" button. This button starts the converting process using information initially entered.

    5.   "Directory selector". This button opens up a file manager to navigate to different directories to save to following conversion. 

    6.   "Reset directory". This button reverts to "Folder to save" input to the default of `"$path to desktop/MyPlaylist"`

