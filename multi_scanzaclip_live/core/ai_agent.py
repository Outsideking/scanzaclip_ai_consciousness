def decide_action(emotion):
    if emotion == "sad":
        action = "cheer_up_user"
        response_text = "Don't worry, everything will be fine!"
    elif emotion == "happy":
        action = "observe"
        response_text = "You seem happy, observing environment."
    else:
        action = "observe"
        response_text = "Observing environment."
    return action, response_text
