import ffmpeg
import subprocess

def convert():
    all_songs = [
            {
                'url': 'https://www.youtube.com/watch?v=1ovA4pShOzw',
                'name': 'InTheCut.mp3'
            },
            {
                'url': 'https://www.youtube.com/watch?v=GLBqrDDCoJU',
                'name': 'FloorIt.mp3'
            },
            {
                'url': 'https://www.youtube.com/watch?v=wiiJ0n_z5nk',
                'name': 'NoRoleModelzKendrick.mp3'
            },
            {
                'url': 'https://www.youtube.com/watch?v=BrUmPkro5sk',
                'name': 'BlackFriday.mp3'
            },
            {
                'url': 'https://www.youtube.com/watch?v=afsh5w4P88o',
                'name': 'MissTheRageReversed.mp3'
            },
    ]


    base_command = ['youtube-dl', '-x', '--audio-format', 'mp3', '--ffmpeg-location', '.', '-o']

    for song in all_songs[2:5]:
        url = song['url']
        name = 'mp3s/' + song['name']
        cmd = base_command.copy()
        cmd.append(name)
        cmd.append(url)
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        print(res)




convert()
