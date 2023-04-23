import psutil
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    MemoryUsgae = psutil.virtual_memory().percent
    CPUUsage = psutil.cpu_percent()
    
    if MemoryUsgae > 80 or CPUUsage > 80:
        return f"Server is overloaded with Memory Usage {MemoryUsgae}% and CPU Usage {CPUUsage}%"

    return f"Server is running with Memory Usage {MemoryUsgae}% and CPU Usage {CPUUsage}%"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')