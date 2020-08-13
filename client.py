import socketio
import serial
import time
import string
import pynmea2




while True:
 port="/dev/ttyAMA0"
 ser=serial.Serial(port, baudrate=9600, timeout=0.5)
 dataout = pynmea2.NMEAStreamReader()
 newdata=ser.readline()

 if newdata[0:6] == "$GPRMC":
  newmsg=pynmea2.parse(newdata)
  lat=newmsg.latitude
  lng=newmsg.longitude
  gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
  print(gps)

sio = socketio.Client()

@sio.on('connect')
def connect():
    print('Connection established')
    sio.emit('updateLocation', {
        "latitude": '-21,2324',
        "longitude": '-50,2332'
    })

sio.connect('http://192.168.0.10:3030?query=1')
sio.wait()

