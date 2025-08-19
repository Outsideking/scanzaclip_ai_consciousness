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
