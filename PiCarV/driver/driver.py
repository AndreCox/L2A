from adafruit_servokit import ServoKit
from RpiMotorLib import rpi_dc_lib
import time
import socketio
import asyncio

# channels
# 0 cam tilt
# 1 cam pan
# 2 steering

# B27 GPIO 27 #13
# B17 GPIO 17 #11

kit = ServoKit(channels=16)
kit.servo[2].angle = 90
kit.servo[1].angle = 90
kit.servo[0].angle = 90

# Motorssetup
MotorLeft = rpi_dc_lib.DRV8833NmDc(27, 13, 50, False, "motor_left")
MotorRight = rpi_dc_lib.DRV8833NmDc(17, 12, 50, False, "motor_right")


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


def runMotor(speed):

    speed = clamp(speed, -100, 100)
    if speed > 0:
        MotorLeft.backward(abs(speed))
        MotorRight.backward(abs(speed))
    elif speed < 0:
        MotorLeft.forward(abs(speed))
        MotorRight.forward(abs(speed))
    else:
        MotorRight.stop()
        MotorLeft.stop()


sio = socketio.Client()


@sio.event
def connect():
    print("connection established")


@sio.event
def steering(data):
    kit.servo[2].angle = clamp(data, 0, 180)


@sio.event
def pan(data):

    kit.servo[1].angle = clamp(data, 0, 180)


@sio.event
def tilt(data):

    kit.servo[0].angle = clamp(data, 0, 180)


@sio.event
def drive(data):
    runMotor(data)


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://localhost:3000")
sio.wait()
