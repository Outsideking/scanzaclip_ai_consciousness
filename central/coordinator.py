from collections import defaultdict

class Coordinator:
    def __init__(self):
        self.tasks = defaultdict(list)

    def store_agent_task(self, agent_name, task):
        self.tasks[agent_name].append(task)

coordinator = Coordinator()
