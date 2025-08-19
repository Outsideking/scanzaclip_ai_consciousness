import pyttsx3
import cv2
import threading

class GUI:
    def __init__(self):
        self.memory_display = self
        self.tts_engine = pyttsx3.init()
        self.video_frame = None
        self.running = True

    def update_gui(self, action, emotion, memory_text=None):
        print(f"[GUI] Action: {action}, Emotion: {emotion}")
        if memory_text:
            print(f"[Memory] {memory_text}")

        # TTS speak action
        self.tts_engine.say(f"Action: {action}, Emotion: {emotion}")
        self.tts_engine.runAndWait()

    def display_video(self, frame):
        cv2.imshow("Scanzaclip Camera Feed", frame)
        cv2.waitKey(1)

    def run_video_loop(self, video_source=0):
        cap = cv2.VideoCapture(video_source)
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.display_video(frame)
        cap.release()
        cv2.destroyAllWindows()

    def run(self):
        threading.Thread(target=self.run_video_loop, daemon=True).start()
        print("[GUI] Running GUI loop...")
        while True:
            pass  # GUI loop
