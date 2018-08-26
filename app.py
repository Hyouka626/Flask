from flask import Flask
from flask import render_template
from flask import jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = "windroc-nwpc-project"
CORS(app, resources=r'/*')
socketio = SocketIO(app, async_mode=None)

# 修改flask自带的模板渲染引擎方式 -> {{  **  }}
app.jinja_env.variable_start_string = '{{  '
app.jinja_env.variable_end_string = '  }}'


@app.route('/')
def hello_world():
    return render_template('index.html')


@socketio.on('progress')
def progress():
    import random
    import time
    for i in range(0, 5):
        jd = random.randint(0, 150)
        print(jd)
        time.sleep(1)
        socketio.sleep(0.1)
        emit('pb', {'data': jd})
    # emit('disconnect')


@socketio.on('close')
def test_connect():
    print("disconnect")
    disconnect()

if __name__ == '__main__':
    # app.run()
    socketio.run(app, host='localhost', port=8080)
