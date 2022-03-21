from cv2 import imshow
import keras as ks
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv
import socketio
from keras.preprocessing.image import img_to_array


ip = "192.168.1.139"

# Load the model
model = ks.models.load_model("experimental_model.h5")

# display stream from ip camera
cap = cv.VideoCapture("http://%s:8080/?action=stream" % ip)
# connecting to the PiCar
sio = socketio.Client()
sio.connect("http://%s:3000" % ip)

sio.emit("tilt", 45)
sio.emit("drive", 0)

# display the captured frame
while True:

    ret, frame = cap.read()
    cv.imshow("frame", frame)
    height, _, _ = frame.shape
    #image = frame[int(height/2):,:,:] 
    image = cv.cvtColor(frame, cv.COLOR_RGB2YUV) 
    blur = cv.GaussianBlur(image, (3, 3), 0)
    image = cv.resize(blur, (200,66), interpolation = cv.INTER_CUBIC)
    image = image / 255
    cv.imshow("image", image)
     
    steering = model.predict(np.array([image]))
    print(steering)
    sio.emit("steer", float(steering[0][0]))

    if cv.waitKey(1) & 0xFF == ord("q"):
        sio.emit("drive", 0)
        break

sio.wait()
