from collections import defaultdict

class Coordinator:
    def __init__(self):
        self.tasks = defaultdict(list)

    def store_agent_task(self, agent_name, task):
        self.tasks[agent_name].append(task)

coordinator = Coordinator()
class Coordinator:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.agent_tasks = {}  # เก็บ task ของทุก agent

    def send_task(self, task):
        agent = task.get("agent","unknown")
        if agent not in self.agent_tasks:
            self.agent_tasks[agent] = []
        self.agent_tasks[agent].append(task)
        # ส่งไป WebSocket server ปกติ
        try:
            self.ws.send(json.dumps(task))
        except:
            pass
