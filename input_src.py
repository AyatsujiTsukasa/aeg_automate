import subprocess
import os
from pydub import AudioSegment


def vid_to_audio(input_path):
    if not os.path.exists('tmp_wkdir'):
        os.makedirs('tmp_wkdir')
    command = "ffmpeg -i {} -ab 160k -ac 1 -ar 48000 -vn tmp_wkdir/audio.wav".format(input_path)
    subprocess.call(command, shell=True)

