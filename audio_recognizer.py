import speech_recognition as sr

class AudioRecognizer(object):

    def __init__(self, wav_path):
        self.recog = sr.Recognizer()
        self.audio_file = sr.AudioFile(wav_path)

    def recognize_start_dur(self, start, dur):
        with self.audio_file as source:
            audio = self.recog.record(source, offset=start, duration=dur)

        return self.recognize(audio)

    def recognize_start_end(self, start, end):
        return self.recognize_start_dur(start, end-start)

    def recognize_all(self):
        with self.audio_file as source:
            audio = self.recog.record(source)

        return self.recognize(audio)


    def recognize(self, audio):
        return self.recog.recognize_sphinx(audio, language="ja-JP")