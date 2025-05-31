import noisereduce as nr
import numpy as np

def reduce_noise(audio, sample_rate=16000):
    # audio should be a 1D numpy array (mono)
    reduced = nr.reduce_noise(y=audio, sr=sample_rate)
    return reduced
