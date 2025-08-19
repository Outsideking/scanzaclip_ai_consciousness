import threading
import time
from gui.gui_interface import GUI
from user_models.user_voice_model import record_audio, speech_to_text, analyze_emotion
from core.ai_agent import decide_action
from core.adaptive_personality import AdaptivePersonalityProfile
from core.long_term_forecast import LongTermBehaviorForecast
from core.multi_agent_collaboration import MultiAgentCoordinator
from core.team_scenario_simulation import TeamScenarioSimulator
from central.coordinator import coordinator

adaptive_profile = AdaptivePersonalityProfile()
forecast_model = LongTermBehaviorForecast(adaptive_profile)
multi_coordinator = MultiAgentCoordinator()
agents_list = ["agent1","agent2","agent3"]
team_simulator = TeamScenarioSimulator(multi_coordinator, forecast_model, agents_list)

def run_robot_agent(user_id, video_source=0):
    gui = GUI()
    threading.Thread(target=gui.run_video_loop, args=(video_source,), daemon=True).start()

    while True:
        audio = record_audio()
        text = speech_to_text(audio)
        emotion = analyze_emotion(text)

        # update adaptive profile
        adaptive_profile.update_event(user_id, emotion)
        profile = adaptive_profile.get_profile(user_id)

        # AI decides action
        action, response_text = decide_action(emotion)
        gui.latest_emotion = emotion
        gui.latest_action = action
        gui.speak(f"Action: {action}, Emotion: {emotion}, Response: {response_text}")

        # 24h scenario simulation
        simulation = team_simulator.simulate_24h(user_id)
        for agent, tasks in simulation.items():
            for t in tasks:
                task_entry = {
                    "agent": agent,
                    "user_id": user_id,
                    "behavior": "team_scenario_simulation",
                    "action": t["action"],
                    "scheduled_hour": t["hour"],
                    "timestamp": time.time()
                }
                # ส่งไป central server
                coordinator.send_task(task_entry)

        time.sleep(5)
from core.behavior_comparator import BehaviorComparator
from central.coordinator import coordinator
while True:
    audio = record_audio()
    text = speech_to_text(audio)
    emotion = analyze_emotion(text)
    action, response_text = decide_action(emotion)

    # อัปเดต adaptive personality
    adaptive_profile.update_event(user_id, emotion)

    # แสดงผลผ่าน GUI
    gui.latest_emotion = emotion
    gui.latest_action = action
    gui.speak(f"Action: {action}, Emotion: {emotion}, Response: {response_text}")

    # 🔥 ใช้งาน comparator
    comparison_results = comparator.compare_behaviors()

    # ดูผลลัพธ์การเปรียบเทียบ
    for agent_name, tasks in comparison_results.items():
        for t in tasks:
            print(f"[Compare] Agent:{agent_name}, User:{t['current_task']['user_id']}, "
                  f"External tasks:{t['external_tasks']}")

    time.sleep(5)
# agents/robot_agent_live_integration.py
import threading, time
from gui.gui_interface import GUI
from user_models.user_voice_model import record_audio, speech_to_text, analyze_emotion
from core.behavior_comparator import BehaviorComparator
from core.mock_external_db import MockExternalDB
from central.genai_client import send_consciousness
from central.coordinator import coordinator
from core.adaptive_personality import AdaptivePersonalityProfile
from core.ai_agent import decide_action    # existing simple decision function

def run_robot_agent(user_id, video_source=0):
    gui = GUI()
    threading.Thread(target=gui.run_video_loop, args=(video_source,), daemon=True).start()

    # สร้าง external DB mock และ comparator
    external_db = MockExternalDB()
    comparator = BehaviorComparator(coordinator, external_db)

    adaptive_profile = AdaptivePersonalityProfile()

    while True:
        audio = record_audio()
        text = speech_to_text(audio)
        emotion = analyze_emotion(text)
        action, response_text = decide_action(emotion)

        # update local profile and coordinator (local memory)
        adaptive_profile.update_event(user_id, emotion)
        task_entry = {
            "agent": "agent_live",
            "user_id": user_id,
            "action": action,
            "emotion": emotion,
            "timestamp": time.time()
        }
        # ส่งไป central coordinator (local store)
        try:
            coordinator.send_task(task_entry)
        except Exception as e:
            print("[Agent] failed to send task to coordinator:", e)

        # ทำการเปรียบเทียบพฤติกรรมกับฐานข้อมูลภายนอก
        comparison = comparator.compare_behaviors()

        # สร้าง payload จิตรสำนึก (consciousness) เพื่อส่งให้ GENAI
        payload = {
            "agent_task": task_entry,
            "adaptive_profile": adaptive_profile.get_profile(user_id),
            "comparison_summary": comparison,
            "note": "Auto-sent by robot_agent_live_integration"
        }

        # ส่งเข้า GENAI
        result = send_consciousness(payload)
        if result.get("ok"):
            print("[GENAI] sent successfully:", result.get("status_code"))
        else:
            print("[GENAI] send failed:", result.get("error"))

        # Update GUI and speak
        gui.latest_emotion = emotion
        gui.latest_action = action
        gui.speak(f"{response_text}")

        # ระยะเวลา loop ปรับได้ตามต้องการ
        time.sleep(5)
