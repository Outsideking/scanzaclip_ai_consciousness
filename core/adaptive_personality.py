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
        
class AdaptivePersonalityProfile:
    def __init__(self):
        self.user_profiles = {}

    def update_event(self, user_id, emotion):
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {"happy":0, "sad":0, "neutral":0}
        self.user_profiles[user_id][emotion] += 1

    def get_profile(self, user_id):
        if user_id not in self.user_profiles:
            return {"happy":0, "sad":0, "neutral":0}
        total = sum(self.user_profiles[user_id].values())
        profile = {k: v/total for k,v in self.user_profiles[user_id].items()} if total>0 else self.user_profiles[user_id]
        return profile
