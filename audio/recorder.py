import sounddevice as sd

def record_audio(duration=15, sample_rate=16000):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    return audio.flatten()
