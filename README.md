# 🎙️ Speaker Detection and Identification System

This project detects the **number of speakers** in real-time audio and identifies each speaker by matching their voice against a known voice database.

## ✅ Current Features

- 🔴 Live audio recording via microphone (default 15 seconds)  
- 🧼 Noise reduction using `noisereduce`  
- 🗣️ Voice Activity Detection (VAD) using `webrtcvad`  
- 📂 Modular Python codebase with clean separation of concerns  
- 🎤 Speaker diarization support using `pyannote-audio` (partially integrated)  

## 📁 Project Structure

```
speaker_identification/
├── audio/                 # Handles recording and noise reduction
├── diarization/ # Speaker diarization logic using pyannote-audio
├── vad/                   # Voice Activity Detection module
├── utils/                 # Config settings
├── main.py                # Runs the full pipeline
├── requirements.txt       # Python dependencies
└── .gitignore # Git ignore file
```


## 🚀 How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/speaker_identification.git
    cd speaker_identification
    ```

2. **Create and activate a virtual environment:**

    - On Linux/macOS:

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      python -m venv venv
      venv\Scripts\activate
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

- 🧠 **Enhance speaker diarization** for better accuracy and realtime processing  
- 🎼 Implement **feature extraction** with `librosa` for improved speaker embeddings  
- 🔐 Develop a **speaker identification** module leveraging `SpeechBrain` for voice matching  
- 📊 Add **visualization** of diarization results (e.g., speaker timeline plots)  
- 🧪 Optimize **model compatibility** by managing PyTorch and pyannote versions  

---

