class BehaviorComparator:
    def __init__(self, coordinator, external_db=None):
        """
        coordinator: central/coordinator object
        external_db: สามารถเชื่อม database ภายนอก (เช่น SQL, MongoDB)
        """
        self.coordinator = coordinator
        self.external_db = external_db

    def fetch_all_behaviors(self):
        # ดึงจาก central coordinator
        central_data = self.coordinator.agent_tasks

        # ดึงจาก external DB (placeholder)
        external_data = {}
        if self.external_db:
            # สมมติ external_db.query() คืนค่า dict {user_id: tasks}
            external_data = self.external_db.query("SELECT * FROM behaviors")

        return central_data, external_data

    def compare_behaviors(self):
        central_data, external_data = self.fetch_all_behaviors()

        comparison_results = {}
        for agent, tasks in central_data.items():
            comparison_results[agent] = []
            for t in tasks:
                user_id = t.get("user_id")
                external_tasks = external_data.get(user_id, []) if external_data else []
                comparison_results[agent].append({
                    "current_task": t,
                    "external_tasks": external_tasks
                })
        return comparison_results
        # core/behavior_comparator.py
from typing import Dict, Any, Optional
import time

class BehaviorComparator:
    """
    ดึงข้อมูลพฤติกรรมจาก central coordinator และ external DB (ถ้ามี)
    แล้วคืนผลเปรียบเทียบเป็นโครงสร้างที่นำไปใช้ต่อได้
    """
    def __init__(self, coordinator, external_db=None):
        """
        coordinator: central.coordinator.Coordinator instance (มี attribute agent_tasks หรือ method ให้ดึง)
        external_db: object ที่มี method query_behaviors() -> Dict[user_id, List[task_dict]]
        """
        self.coordinator = coordinator
        self.external_db = external_db

    def fetch_central_behaviors(self) -> Dict[str, Any]:
        """
        คาดว่า coordinator.agent_tasks เป็น dict: { agent_name: [task_entry, ...] }
        แต่ถ้าโครงสร้างต่างให้ปรับตามความเป็นจริง
        """
        try:
            return getattr(self.coordinator, "agent_tasks", {}) or {}
        except Exception as e:
            print("[BehaviorComparator] error fetching central behaviors:", e)
            return {}

    def fetch_external_behaviors(self):
        if not self.external_db:
            return {}
        try:
            return self.external_db.query_behaviors()
        except Exception as e:
            print("[BehaviorComparator] error fetching external behaviors:", e)
            return {}

    def compare_single(self, current_task: dict, external_tasks: list) -> dict:
        """
        เปรียบเทียบ task เดียวกับรายการจาก external DB
        คืนค่า summary: similarity score, matches, notes
        (ที่นี่เป็นตัวอย่าง heuristic ง่าย ๆ — ปรับตามต้องการ)
        """
        score = 0.0
        matches = []
        notes = []

        curr_action = current_task.get("action")
        curr_emotion = current_task.get("emotion")
        curr_user = current_task.get("user_id")

        for ext in external_tasks:
            # heuristic: action exact match + emotion match
            ext_action = ext.get("action")
            ext_emotion = ext.get("emotion")
            s = 0
            if ext_action == curr_action:
                s += 0.6
                matches.append({"type":"action", "value": ext_action})
            if ext_emotion == curr_emotion:
                s += 0.3
                matches.append({"type":"emotion", "value": ext_emotion})
            # temporal similarity (within same hour)
            try:
                if abs((ext.get("timestamp",0) - current_task.get("timestamp",0)) ) < 3600:
                    s += 0.1
            except:
                pass
            if s > 0:
                score = max(score, s)

        if score == 0.0:
            notes.append("No similar historical tasks found")
        return {
            "current_task": current_task,
            "external_matches": matches,
            "similarity_score": round(score, 3),
            "notes": notes
        }

    def compare_behaviors(self) -> dict:
        """
        ดึงข้อมูลจากทั้งสองแหล่งและทำการเปรียบเทียบ
        Return structure:
        {
          agent_name: [ { current_task, external_matches, similarity_score, notes }, ... ],
          ...
        }
        """
        central = self.fetch_central_behaviors()
        external = self.fetch_external_behaviors()

        result = {}
        for agent, tasks in central.items():
            result[agent] = []
            for t in tasks:
                user_id = t.get("user_id")
                external_for_user = external.get(user_id, []) if external else []
                comp = self.compare_single(t, external_for_user)
                result[agent].append(comp)
        # meta
        return {
            "timestamp": time.time(),
            "comparison": result
                }
