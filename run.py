from flask import Flask
from datetime import datetime  # 导入获取当前时间的模块

app = Flask(__name__)

# 根路径返回 "Hello world!"
@app.route('/')
def hello_world():
    return 'Hello world!'

# 新增 /time 路由，返回当前时间
@app.route('/time')
def get_time():
    # 获取当前时间并格式化为 YYYY-MM-DD HH:MM:SS 格式
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return "Current time: {}".format(current_time)

# 运行Flask应用
app.run(host='0.0.0.0', port=8080, debug=True)
