import threading
import time
from gui.gui_interface import GUI
from user_models.user_voice_model import record_audio, speech_to_text, analyze_emotion
from core.ai_agent import decide_action
from central.coordinator import coordinator

def run_robot_agent(user_id, video_source=0):
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

        # ส่ง task/behavior ไป central server
        task = {
            "user_id": user_id,
            "action": action,
            "emotion": emotion,
            "response_text": response_text,
            "timestamp": time.time()
        }
        coordinator.send_task(task)
        print(f"[Agent] {task}")

        time.sleep(5)  # interval
