class LongTermBehaviorForecast:
    def __init__(self, user_model):
        self.user_model = user_model

    def forecast_next_24h(self, user_id, interval_hours=1):
        history = self.user_model.user_profiles[user_id]["history"][-200:]
        forecast = []
        for h in range(24 // interval_hours):
            emotions = [e["emotion"] for e in history]
            predicted = "sad" if emotions.count("sad") > len(history)/3 else "neutral"
            forecast.append({"hour": h, "predicted_emotion": predicted})
        return forecast

    def decide_full_day_strategy(self, user_id, agent_name):
        forecast = self.forecast_next_24h(user_id)
        actions = []
        for f in forecast:
            act = "cheer_up_user" if f["predicted_emotion"]=="sad" else "observe"
            actions.append({"hour": f["hour"], "action": act, "emotion": f["predicted_emotion"]})
        return actions
class LongTermBehaviorForecast:
    def __init__(self, adaptive_profile):
        self.adaptive_profile = adaptive_profile

    def forecast_next_hours(self, user_id, hours=24):
        profile = self.adaptive_profile.get_profile(user_id)
        forecast = []
        for h in range(hours):
            if profile.get("sad",0) > 0.5:
                action = "cheer_up_user"
            else:
                action = "observe"
            forecast.append({"hour":h, "action":action})
        return forecast
