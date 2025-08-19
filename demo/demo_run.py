import threading
import time
from gui_interface import GUI
from user_voice_model import record_audio, speech_to_text, analyze_emotion

def run_demo(user_id="user_demo"):
    gui = GUI()

    # Start video feed
    threading.Thread(target=gui.run_video_loop, args=(0,), daemon=True).start()

    while True:
        # Record audio (placeholder)
        audio = record_audio(duration=2)
        text = speech_to_text(audio)
        emotion = analyze_emotion(text)

        # AI decides action based on emotion
        if emotion == "sad":
            action = "cheer_up_user"
            response_text = "Don't worry, everything will be fine!"
        else:
            action = "observe"
            response_text = "Observing environment."

        # TTS speak action
        gui.speak(f"Action: {action}, Emotion: {emotion}, Response: {response_text}")
        print(f"[Demo] Action: {action}, Emotion: {emotion}, Response: {response_text}")

        time.sleep(5)  # simulate interval
        

if __name__ == "__main__":
    run_demo()
