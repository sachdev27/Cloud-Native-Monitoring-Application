import psutil
from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    MemoryUsgae = psutil.virtual_memory().percent
    CPUUsage = psutil.cpu_percent()
    Message = ""
    if MemoryUsgae > 80 or CPUUsage > 80:
        Message = f"Server is overloaded with Memory Usage {MemoryUsgae}% and CPU Usage {CPUUsage}%"
    return render_template('index.html',cpu_metric=CPUUsage,mem_metric=MemoryUsgae,message=Message)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')