import threading
import time
from gui_interface import GUI
from user_voice_model import record_audio, speech_to_text, analyze_emotion
from ai_agent import decide_action

def run_live_demo(video_source=0):
    gui = GUI()
    threading.Thread(target=gui.run_video_loop, args=(video_source,), daemon=True).start()

    while True:
        audio = record_audio()
        text = speech_to_text(audio)
        emotion = analyze_emotion(text)
        action, response_text = decide_action(emotion)

        gui.latest_emotion = emotion
        gui.latest_action = action

        gui.speak(f"Action: {action}, Emotion: {emotion}, Response: {response_text}")
        print(f"[Live Demo] Action: {action}, Emotion: {emotion}, Response: {response_text}")

        time.sleep(5)  # interval between analysis

if __name__ == "__main__":
    run_live_demo(video_source=0)  # เปลี่ยนเป็น scanzaclip camera index หรือ URL
