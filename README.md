This is a simple python program that can be used to download songs from youtube. It relies on youtube-dl (which relies on ffmpeg) 
You will have to install youtube-dl (instructions below). The program should aotomatically download and unzip the ffmpeg binary to be used here

Dev setup:
- Create a virtual environment
    - python -m venv /path/to/env
- Activate it
    - /path/to/env/Scripts/Activate.bat (for windows)
    - source ~/Desktop/virtual_environments/youtube2mp3/Scripts/activate (for liunux)
- Install youtube-dl
    - Youtube-dl is broken because of an update from youtube and the package needs to be installed from here
    - pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
    - Here is info on youtube-dl
        - https://github.com/ytdl-org/youtube-dl/issues/31530#issuecomment-1435477247
        - https://github.com/ytdl-org/youtube-dl/issues/31530

Running the program
- The program takes songs from a provided input file (and defaults to using example_input_file.txt in the case that a file of songs is not provided)

# Start of file
song_url
name_you_want_for_downloaded_file
song_url
name_you_want_for_downloaded_file
# ...more songs can follow

- The program will output downloaded mp3s to the outputs directory
- Run with the following command:
    - python -m script.py songListFileArg