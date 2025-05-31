import webrtcvad

class VAD:
    def __init__(self, mode=3):
        self.vad = webrtcvad.Vad(mode)

    def is_speech(self, audio_bytes, sample_rate=16000):
        return self.vad.is_speech(audio_bytes, sample_rate)