import socketio
import time

sio = socketio.Client()
sio.connect('http://192.168.50.5:3000')

# steer center
center = 78

sio.emit('steer', center)
sio.emit('drive', 50)
time.sleep(7.1)
sio.emit('drive', 0)

sio.emit('steer', 20)
sio.emit('drive', 50)
time.sleep(1.2)
sio.emit('drive', 0)


#time.sleep(0.5)
sio.emit('drive', -50)
sio.emit('steer', 128)
time.sleep(1.2)
sio.emit('drive', 0)

#time.sleep(0.5)
sio.emit('drive', 50)
sio.emit('steer', 20)
time.sleep(1)

sio.emit('steer', center)
sio.emit('drive', 0)

sio.emit('steer', center)
sio.emit('drive', 50)
time.sleep(7.1)
sio.emit('drive', 0)

time.sleep(2)



