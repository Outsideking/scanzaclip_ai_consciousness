import cv2
import pyttsx3
import threading

class GUI:
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.running = True

    def display_video(self, frame):
        cv2.imshow("Scanzaclip Live Demo", frame)
        cv2.waitKey(1)

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def run_video_loop(self, video_source=0):
        cap = cv2.VideoCapture(video_source)  # 0 = webcam / scanzaclip camera feed
        while self.running:
            ret, frame = cap.read()
            if ret:
                self.display_video(frame)
        cap.release()
        cv2.destroyAllWindows()
