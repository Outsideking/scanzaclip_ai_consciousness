from core.team_scenario_simulation import TeamScenarioSimulator
from core.adaptive_personality import AdaptivePersonalityProfile
from core.long_term_forecast import LongTermBehaviorForecast
from core.multi_agent_collaboration import MultiAgentCoordinator
from user_models.user_voice_model import record_audio, speech_to_text, analyze_emotion
import websocket, json, time

adaptive_profile = AdaptivePersonalityProfile()
forecast_model = LongTermBehaviorForecast(adaptive_profile)
multi_coordinator = MultiAgentCoordinator()
agents = ["agent1","agent2","agent3"]
team_simulator = TeamScenarioSimulator(multi_coordinator, forecast_model, agents)

central_ws_url = "ws://localhost:8080"  # ตัวอย่าง URL

def run_team_simulation(user_id, gui):
    ws = websocket.WebSocketApp(central_ws_url)
    while True:
        # Real-time audio
        audio = record_audio(duration=2)
        text = speech_to_text(audio)
        voice_emotion = analyze_emotion(text)
        adaptive_profile.update_event(user_id, voice_emotion)
        profile = adaptive_profile.get_profile(user_id)

        # 24h scenario simulation
        simulation = team_simulator.simulate_24h(user_id)
        for agent, tasks in simulation.items():
            for t in tasks:
                multi_coordinator.store_agent_task(agent, t)
                memory_entry = {
                    "agent": agent,
                    "user_id": user_id,
                    "behavior": "team_scenario_simulation",
                    "action": t["action"],
                    "scheduled_hour": t["hour"],
                    "weight": t["weight"],
                    "timestamp": time.time()
                }
                # ส่งไป central server
                try: ws.send(json.dumps(memory_entry))
                except: pass
                gui.update_gui(t["action"], t["action"], gui.memory_display.toPlainText())
        time.sleep(60)
git add agents/ gui/ user_models/ requirements.txt run_system.py
git commit -m "Add GUI + TTS + real-time audio/video integration"
git push origin main
