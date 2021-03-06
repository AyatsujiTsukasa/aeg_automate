import sys
import shutil
from input_src import vid_to_audio
from segments import seg_detection
from ass_support import ASSGenerator



def create_ass(aggressiveness, vid_file_path):
    vid_to_audio(vid_file_path)
    segs = seg_detection(aggressiveness, "tmp_wkdir/audio.wav")

    ass_gen = ASSGenerator()
    ass_gen.create_ass_file(segs, vid_file_path)

    shutil.rmtree('tmp_wkdir')
    


def main(args):
    if len(args) != 2:
        sys.stderr.write('Usage: aeg.py <aggressiveness> <path to video file>\n')
        sys.exit(1)

    aggressiveness = int(args[0])
    vid_file_path = args[1]
    
    create_ass(aggressiveness, vid_file_path)


if __name__ == '__main__':
    main(sys.argv[1:])