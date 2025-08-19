from collections import defaultdict
import time

class AdaptivePersonalityProfile:
    def __init__(self):
        self.user_profiles = defaultdict(lambda: {
            "traits": defaultdict(float),
            "preferences": defaultdict(float),
            "history": []
        })

    def update_event(self, user_id, emotion, activity=None):
        self.user_profiles[user_id]["history"].append({
            "emotion": emotion,
            "activity": activity,
            "timestamp": time.time()
        })
        self._adaptive_evolution(user_id)

    def _adaptive_evolution(self, user_id):
        history = self.user_profiles[user_id]["history"][-100:]
        counts = defaultdict(int)
        for h in history: counts[h["emotion"]] += 1
        total = len(history)
        for emotion, c in counts.items():
            self.user_profiles[user_id]["traits"][emotion] = c / total

    def get_profile(self, user_id):
        return self.user_profiles[user_id]
