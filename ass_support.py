import time
import os
import codecs


class ASSGenerator(object):
    def __init__(self):
        self.ass_file_format = open('ass_file_format.txt').read()
        self.ass_track_format = open('ass_track_format.txt').read()

    def __format_time(self, t):
        hms = time.strftime('%H:%M:%S', time.gmtime(t))
        millisec = int(t % 1 * 100000)
        return "{}.{}".format(hms, millisec)

    def create_track_line(self, time_start, time_end):
        return self.ass_track_format.format(self.__format_time(time_start), self.__format_time(time_end))

    def create_ass_file(self, segs, vid_file_path):
        file_content = self.ass_file_format.replace("{video_file_path}", vid_file_path)
        for seg in segs:
            file_content += self.create_track_line(seg[0], seg[1]) + '\n'

        ass_file_path = os.path.splitext(vid_file_path)[0] + '_generated.ass'
        with codecs.open(ass_file_path, 'w', encoding='utf-8') as f:    
            f.write(file_content)
            f.close()

        folder_path = vid_file_path.rsplit('\\', 1)[0]
        os.startfile(folder_path)
        