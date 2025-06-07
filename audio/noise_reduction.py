import noisereduce as nr

def reduce_noise(audio, sample_rate=16000):
    reduced = nr.reduce_noise(y=audio, sr=sample_rate)
    return reduced