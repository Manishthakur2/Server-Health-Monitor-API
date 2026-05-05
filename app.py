from flask import Flask, jsonify
import psutil
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "app": "Server Health Monitor",
        "version": "1.0",
        "status": "running"
    })

@app.route('/health')
def health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": memory.percent,
        "memory_available_gb": round(memory.available / (1024**3), 2),
        "disk_percent": disk.percent,
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "db_host": os.getenv("DB_HOST", "not set")
    })

@app.route('/ping')
def ping():
    return jsonify({"status": "pong"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
