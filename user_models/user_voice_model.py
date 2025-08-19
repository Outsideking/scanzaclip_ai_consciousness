import pyaudio
import numpy as np

CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 2

def record_audio(duration=RECORD_SECONDS):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    frames = []
    for _ in range(int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return b''.join(frames)

def speech_to_text(audio):
    # ตัวอย่าง placeholder
    return "user speech text"

def analyze_emotion(text):
    # ตัวอย่าง simple
    if "sad" in text.lower(): return "sad"
    return "neutral"
git add agents/ gui/ user_models/ requirements.txt run_system.py
git commit -m "Add GUI + TTS + real-time audio/video integration"
git push origin main
