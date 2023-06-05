import subprocess
import sys
import os

example_input_file = "example_input_file.txt"

# Determines if the script is running in a virtual environment
def in_venv():
    return sys.prefix != sys.base_prefix

# Determines if ffmpeg folder already exists
def find_ffmpeg_folder():
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        for dir in dirs:
            if "ffmpeg" in dir:
                return os.path.join(dir)
    return None

# Downloads fffmpeg and unzips it
def download_ffmpeg():
    download_name = 'ffmpeg-release-essentials'

    url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'
    cmd = ['curl', '-L', url, '-o', download_name]
    res = subprocess.run(cmd, stdout=subprocess.PIPE)

    cmd = ['unzip', download_name]
    res = subprocess.run(cmd, stdout=subprocess.PIPE)

    cmd = ['rm', download_name]
    res = subprocess.run(cmd, stdout=subprocess.PIPE)

# Parses the input file into a list of dictionaries where each entry is a song with two attributes - url and name
def read_file_to_dictionary(file_path):
    entries = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        for i in range(0, num_lines, 2):
            url = lines[i].strip()
            name = lines[i+1].strip()
            song_data = {
                'url': url,
                'name': name
            }
            entries.append(song_data)
    return entries

# Uses youtube-dl to download songs from the input file
def convert(ffmpeg_bin, input_file):
    all_songs = read_file_to_dictionary(input_file)

    for song in all_songs:
        base_command = ['youtube-dl', '-x', '--audio-format', 'mp3', '--ffmpeg-location', ffmpeg_bin, '-o', f"outputs/{song['name']}.%(ext)s"]
        cmd = base_command.copy()
        cmd.append(song['url'])
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        # print(res)



## MAIN ##
def main():
    if in_venv():
        print('In virtual environment')

        songs_file = example_input_file

        if len(sys.argv) > 1:
            songs_file = sys.argv[1]

        print('Using songs file: ' + songs_file) 

        ffmpeg_folder = find_ffmpeg_folder()

        if not ffmpeg_folder:
            print('Downloading ffmpeg')
            download_ffmpeg()
        else:
            print('Have ffmpeg folder')
        
        ffmpeg_folder = find_ffmpeg_folder()
        ffmpeg_bin = ffmpeg_folder + '/bin/'
        print('ffmpeg binary: ' + ffmpeg_bin)

        try:
            convert(ffmpeg_bin, songs_file)
        except Exception as e: 
            print(e)
    else:
        print('Not in virtual environment. See README.md for instructions.')
        exit(1)

main()
