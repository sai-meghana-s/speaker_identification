from audio.recorder import record_audio
from audio.noise_reduction import reduce_noise
from vad.vad import VAD
from utils.config import SAMPLE_RATE, DURATION

import soundfile as sf

def main():
    # Step 1: Record Audio
    audio = record_audio(duration=DURATION, sample_rate=SAMPLE_RATE)

    # Step 2: Reduce Noise
    clean_audio = reduce_noise(audio, sample_rate=SAMPLE_RATE)

    import numpy as np

    # Convert to bytes in 20ms chunks (required by webrtcvad)
    frame_duration = 20  # ms
    frame_size = int(SAMPLE_RATE * frame_duration / 1000)  # samples per frame
    num_frames = len(clean_audio) // frame_size
    vad=VAD()
    speech_detected = False
    for i in range(num_frames):
        frame = clean_audio[i * frame_size:(i + 1) * frame_size]
        if len(frame) != frame_size:
            continue
        frame_bytes = frame.astype(np.int16).tobytes()
        if vad.is_speech(frame_bytes, sample_rate=SAMPLE_RATE):
            speech_detected = True
            break

    print("Speaking Detected" if speech_detected else "No Speech Detected")


    # Step 4: Save Output for Verification
    sf.write("output_clean.wav", clean_audio, SAMPLE_RATE)
    print("Saved: output_clean.wav")

if __name__ == "__main__":
    main()
