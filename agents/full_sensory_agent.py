# full_sensory_agent.py
import time

def run_full_sensory_agent(agent_name, gui):
    """รับ video/audio/presence data จาก scanzaclip และส่งไป GUI"""
    while True:
        # ตัวอย่าง: รับข้อมูล sensory จาก scanzaclip
        sensory_data = {"video": "frame_data", "audio": "audio_chunk"}
        gui.update_gui("sensory_update", sensory_data)
        time.sleep(1)
