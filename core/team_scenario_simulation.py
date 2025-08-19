from collections import defaultdict
import numpy as np

class TeamScenarioSimulator:
    def __init__(self, coordinator, forecast_model, agents):
        self.coordinator = coordinator
        self.forecast_model = forecast_model
        self.agents = agents

    def simulate_24h(self, user_id):
        forecast = self.forecast_model.forecast_next_24h(user_id)
        simulation_results = defaultdict(list)
        for hour, f in enumerate(forecast):
            for agent in self.agents:
                action = "cheer_up_user" if f["predicted_emotion"]=="sad" else "observe"
                weight = np.random.rand()
                simulation_results[agent].append({"hour": hour, "action": action, "weight": weight})
        # Conflict resolution
        for hour in range(24):
            hour_tasks = [(agent,t) for agent,tasks in simulation_results.items() for t in tasks if t["hour"]==hour]
            if len(hour_tasks)>1:
                hour_tasks.sort(key=lambda x:x[1]["weight"], reverse=True)
                winner = hour_tasks[0]
                for loser in hour_tasks[1:]:
                    loser[1]["action"]="wait"
        return simulation_results
