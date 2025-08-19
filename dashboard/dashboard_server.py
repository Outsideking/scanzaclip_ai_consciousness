from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
from central.coordinator import coordinator

app = Flask(__name__)
socketio = SocketIO(app)

# ส่งข้อมูล real-time จาก central coordinator ไป dashboard
def broadcast_tasks():
    import time
    while True:
        for agent, tasks in coordinator.agent_tasks.items():
            socketio.emit('update', {'agent': agent, 'tasks': tasks})
        time.sleep(2)  # interval

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=broadcast_tasks, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=5000)
