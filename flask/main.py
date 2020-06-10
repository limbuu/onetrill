import logging
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def login():
    return render_template('login.html', name='New User')

@app.route('/login', methods=['POST'])
def login_form():
    first_name = request.form['fname']        
    last_name = request.form['lname']   
    name = first_name + ' ' + last_name
    ## TO DO  
    return render_template('home.html', name=name)

@app.route('/logout')
def logout():
    return render_template('logout.html', name='New User')
    
@app.route('/chat')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    print('received join request: ',data)
    send(username + ' has entered the room.', room=room)
    
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    print('received leave request: ',data)
    send(username + ' has left the room.', room=room)
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    socketio.run(app, debug=True)