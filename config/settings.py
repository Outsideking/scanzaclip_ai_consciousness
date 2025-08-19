central_ws_url = "ws://localhost:8080"
agents = ["agent1", "agent2", "agent3"]
# 1. สร้าง repo ใหม่ (หรือใช้ repo เดิม)
git init
git remote add origin https://github.com/<username>/scanzaclip_ai_consciousness.git

# 2. เพิ่มไฟล์ทั้งหมด
git add .

# 3. Commit
git commit -m "Initial commit: full multi-scanzaclip AI consciousness system with GUI/TTS/real-time audio/video + scenario simulation + adaptive personality + central sync"

# 4. Push ขึ้น GitHub
git branch -M main
git push -u origin main
# Central server URL
central_ws_url = "ws://localhost:8080"  # เปลี่ยนเป็น server จริง

# รายชื่อ agents
agents = ["agent1", "agent2", "agent3"]

# camera sources
# สามารถใช้ index ของ webcam หรือ URL ของ scanzaclip network feed
video_sources = [
    0,  # webcam 0
    1,  # webcam 1
    "rtsp://192.168.1.101:554/stream1",  # ตัวอย่าง scanzaclip camera network
    "rtsp://192.168.1.102:554/stream1"
]

# users
users = ["user_001", "user_002", "user_003"]
