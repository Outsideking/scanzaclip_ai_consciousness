import cv2
import pyttsx3
import threading

class GUI:
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.running = True
        self.latest_emotion = "neutral"
        self.latest_action = "observe"

    def display_video(self, frame):
        # overlay action & emotion
        cv2.putText(frame, f"Action: {self.latest_action}", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"Emotion: {self.latest_emotion}", (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow("Scanzaclip Live Feed", frame)
        cv2.waitKey(1)

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def run_video_loop(self, video_source=0):
        cap = cv2.VideoCapture(video_source)
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.display_video(frame)
        cap.release()
        cv2.destroyAllWindows()
