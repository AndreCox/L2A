import socketio
import time

sio = socketio.Client()
sio.connect('http://192.168.50.5:3000')

sio.emit('steer', 74)
time.sleep(2)
sio.emit('drive', 50)
time.sleep(7.1)
sio.emit('drive', 0)

sio.emit('steer', 74)
time.sleep(2)
sio.emit('steer', 20)
sio.emit('drive', 50)
time.sleep(3)
sio.emit('drive', 0)
sio.emit('steer', 74)

sio.emit('drive', 50)
time.sleep(7.1)
sio.emit('drive', 0)






exit()
