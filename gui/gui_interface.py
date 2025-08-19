class GUI:
    def __init__(self):
        self.memory_display = self

    def update_gui(self, action, emotion, memory_text=None):
        print(f"[GUI] Action: {action}, Emotion: {emotion}")

    def run(self):
        print("[GUI] Running GUI loop...")
        while True:
            pass  # GUI loop
