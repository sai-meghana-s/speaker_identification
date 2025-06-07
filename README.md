# 🎙️ Speaker Detection and Identification System

This project detects whether someone is speaking in real-time and extracts only the speech segments using Voice Activity Detection (VAD).

## ✅ Current Features 

- 🔴 Live audio recording via microphone 
- 🧼 Noise reduction using `noisereduce`  
- 🗣️ Voice Activity Detection (VAD) using `webrtcvad`  
- ✂️ Extraction of speech-only segments to `speech_only.wav`  
- 📂 Modular Python codebase
- 🎤 Speaker diarization support using `pyannote-audio` 

## 📁 Project Structure

```
speaker_identification/
├── audio/                 # Handles recording and noise reduction
├── vad/                   # Voice Activity Detection module
├── diarization/           # Speaker diarization logic using pyannote-audio
├── utils/                 # Config settings
├── vad_pipeline.py        # Runs recording, noise reduction, VAD
├── main.py                # Entry point that calls the pipeline
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

## 🔐 Authentication for Diarization

- The diarization step uses Hugging Face's `pyannote-audio` models, which require a **Hugging Face API token**.
- Create a free account at [huggingface.co](https://huggingface.co), then generate an access token under **Settings > Access Tokens**.
- Save your token securely and update the `diarization.py` file to use it:

    ```python
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization@2.1", 
        use_auth_token="YOUR_HUGGINGFACE_TOKEN"
    )
    ```

---

## 📌 Planned Next Steps

- 🎼 Implement **feature extraction** with `librosa` for improved speaker embeddings  
- 🔐 Develop a **speaker identification** module leveraging `SpeechBrain` for voice matching   

---
