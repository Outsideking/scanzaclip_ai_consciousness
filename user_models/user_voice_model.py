def record_audio(duration=2):
    return b"audio_chunk_data"

def speech_to_text(audio):
    return "user speech text"

def analyze_emotion(text):
    # simple example
    if "sad" in text.lower(): return "sad"
    return "neutral"
