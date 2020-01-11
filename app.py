from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
user = {}
@app.route("/user/<name>")
def index(name):
    return render_template("index.html", name=name)

@socketio.on('add_user')
def add_user(username):
    user[username['username']] = request.sid
    print(user)

@socketio.on('private_message')
def private_message(msg):
    username = user[msg['username']]
    emit('private_message',"hello",room = username)

if __name__ == "__main__":
    socketio.run(app,debug=True,port=8000)
