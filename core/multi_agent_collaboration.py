from collections import defaultdict

class MultiAgentCoordinator:
    def __init__(self):
        self.agent_tasks = defaultdict(list)

    def store_agent_task(self, agent_name, task):
        self.agent_tasks[agent_name].append(task)

    def detect_conflicts(self):
        conflicts = []
        hours_map = defaultdict(list)
        for agent, tasks in self.agent_tasks.items():
            for t in tasks:
                hours_map[t["hour"]].append((agent, t))
        for hour, task_list in hours_map.items():
            if len(task_list) > 1:
                conflicts.append(task_list)
        return conflicts

    def resolve_conflicts(self):
        conflicts = self.detect_conflicts()
        for conflict_group in conflicts:
            sorted_group = sorted(conflict_group, key=lambda x: x[1].get("weight",1.0), reverse=True)
            winner = sorted_group[0]
            for loser in sorted_group[1:]:
                loser[1]["action"] = "wait"
        return self.agent_tasks
        class MultiAgentCoordinator:
    def __init__(self):
        self.agent_tasks = {}

    def store_agent_task(self, agent, task):
        if agent not in self.agent_tasks:
            self.agent_tasks[agent] = []
        self.agent_tasks[agent].append(task)

    def resolve_conflicts(self):
        # simple: remove duplicate action at same hour
        for agent, tasks in self.agent_tasks.items():
            unique_tasks = []
            hours = set()
            for t in tasks:
                if t["hour"] not in hours:
                    unique_tasks.append(t)
                    hours.add(t["hour"])
            self.agent_tasks[agent] = unique_tasks
