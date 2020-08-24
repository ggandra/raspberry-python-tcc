import socketio
import serial
import time
import string
import pynmea2

sio = socketio.Client()
sio.connect('http://192.168.0.10:3030?query=1')

while True:
    port="/dev/ttyAMA0"
    try: 
        ser=serial.Serial(port, baudrate=9600, timeout=2)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline() 
        newval=newdata.decode("utf-8", "replace")
        if newval[0:6] == "$GPRMC":
            newmsg=pynmea2.parse(newval)
            lat=newmsg.latitude
            lng=newmsg.longitude
            gps = "Lat= " + str(lat) + " Long= " + str(lng)
            sio.emit('updateLocation', {
                "latitude": str(lat),
                "longitude": str(lng),
                "id": 1
            })
            print(gps)
    except: 
        pass

