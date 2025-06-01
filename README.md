# 🎙️ Speaker Detection and Identification System

This project detects the **number of speakers** in real-time and identifies each one by matching their voice with a known database.

## ✅ Current Features

- 🔴 Live audio recording via microphone (5 seconds)  
- 🧼 Noise reduction using `noisereduce`  
- 🗣️ Voice Activity Detection (VAD) using `webrtcvad`  
- 📂 Modular Python codebase  

## 📁 Project Structure

```
speaker_identification/
├── audio/                 # Handles recording and noise reduction
├── vad/                   # Voice Activity Detection module
├── utils/                 # Config settings
├── main.py                # Runs the full pipeline
├── requirements.txt       # Python dependencies
```

## 🚀 How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/speaker_identification.git
   cd speaker_identification
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main program:**
   ```bash
   python main.py
   ```

## 📌 Next Steps (Planned)

- 🧠 Speaker diarization using `pyannote-audio`  
- 🎼 Feature extraction with `librosa`  
- 🔐 Speaker identification using `SpeechBrain`
