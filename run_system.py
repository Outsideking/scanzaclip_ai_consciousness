from agents.robot_agent_team_simulation import run_team_simulation
from gui.gui_interface import GUI
import threading

def start_system(user_id):
    gui = GUI()
    threading.Thread(target=run_team_simulation, args=(user_id, gui), daemon=True).start()
    gui.run()

if __name__ == "__main__":
    user_id = "user_001"
    start_system(user_id)
git add agents/ gui/ user_models/ requirements.txt run_system.py
git commit -m "Add GUI + TTS + real-time audio/video integration"
git push origin main
python run_system.py
