from agents.robot_agent_live import run_robot_agent
import threading
from config import settings

def start_live_system(user_id="user_001"):
    for idx, video_source in enumerate(settings.video_sources):
        threading.Thread(target=run_robot_agent, args=(f"{user_id}_{idx}", video_source), daemon=True).start()
    while True:
        pass  # main loop

if __name__ == "__main__":
    start_live_system()
from agents.robot_agent_live import run_robot_agent
import threading
from config import settings

def start_live_system():
    threads = []
    # loop สำหรับทุก user + camera
    for i, user_id in enumerate(settings.users):
        video_source = settings.video_sources[i % len(settings.video_sources)]
        t = threading.Thread(target=run_robot_agent, args=(user_id, video_source), daemon=True)
        t.start()
        threads.append(t)

    # main loop
    while True:
        pass

if __name__ == "__main__":
    start_live_system()
