import websocket
import json

class Coordinator:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.ws = websocket.WebSocketApp(ws_url)
        self.tasks = []

    def send_task(self, task):
        try:
            self.ws.send(json.dumps(task))
        except:
            print("Central server not reachable. Task skipped.")

coordinator = Coordinator("ws://localhost:8080")
