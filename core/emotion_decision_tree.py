class EmotionDecisionTree:
    def __init__(self):
        self.tree = {}

    def add_rule(self, current_emotion, user_state, action, weight=1.0):
        if current_emotion not in self.tree:
            self.tree[current_emotion] = []
        self.tree[current_emotion].append({
            "user_state": user_state,
            "action": action,
            "weight": weight
        })

    def decide_action(self, user_id):
        # ตัวอย่าง simple random pick
        from random import choice
        actions = self.tree.get("neutral", [{"action":"observe","weight":1.0}])
        action = choice(actions)
        return action["action"], "neutral"
