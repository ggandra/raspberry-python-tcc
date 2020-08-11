import socketio

sio = socketio.Client()

@sio.on('connect')
def connect():
    print('Connection established')
    sio.emit('updateLocation', {
        "latitude": '-21,2324',
        "longitude": '-50,2332'
    })

sio.connect('http://localhost:3030?query=1')
sio.wait()

