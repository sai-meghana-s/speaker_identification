from audio.recorder import record_audio
from audio.noise_reduction import reduce_noise
from vad.vad import VAD
from utils.config import SAMPLE_RATE, DURATION

import soundfile as sf
import numpy as np

def run_vad_pipeline():
    audio = record_audio(duration=DURATION, sample_rate=SAMPLE_RATE)
    print(f"Recorded audio shape: {audio.shape}, dtype: {audio.dtype}")

    clean_audio = reduce_noise(audio, sample_rate=SAMPLE_RATE)
    print(f"Clean audio shape: {clean_audio.shape}, dtype: {clean_audio.dtype}")

    frame_duration = 20  # milliseconds
    frame_size = int(SAMPLE_RATE * frame_duration / 1000)
    num_frames = len(clean_audio) // frame_size
    vad = VAD()
    speech_segments = []

    for i in range(num_frames):
        frame = clean_audio[i * frame_size : (i + 1) * frame_size]
        if len(frame) != frame_size:
            continue
        
        frame_int16 = (frame * 32767).astype(np.int16)
        frame_bytes = frame_int16.tobytes()

        if vad.is_speech(frame_bytes, sample_rate=SAMPLE_RATE):
            speech_segments.append(frame)

    if speech_segments:
        speech_audio = np.concatenate(speech_segments)
        sf.write("speech_only.wav", speech_audio, SAMPLE_RATE)
        print("Speaking Detected")
        print("Saved: speech_only.wav")
    else:
        print("No Speech Detected")

if __name__ == "__main__":
    run_vad_pipeline()
