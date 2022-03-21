from cv2 import imshow
import keras as ks
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv
import socketio
from keras.preprocessing.image import img_to_array
import imutils


ip = "192.168.1.139"

# Load the model
model = ks.models.load_model("atlas4.h5")

# display stream from ip camera
cap = cv.VideoCapture("http://%s:8080/?action=stream" % ip)
# connecting to the PiCar
sio = socketio.Client()
sio.connect("http://%s:3000" % ip)

sio.emit("tilt", 45)
sio.emit("drive", 50)

# display the captured frame
while True:
    try:
        ret, frame = cap.read()
        blur = cv.GaussianBlur(frame, (5, 5), 0)
        hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
        # isolate green channel
        mask = cv.inRange(hsv, (40, 20, 40), (100, 255, 250))
        mask = cv.GaussianBlur(mask, (5, 5), 0)
        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)
        mask = cv.GaussianBlur(mask, (5, 5), 0)

        imshow("pre-contor", mask)

        # find contours
        contors = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
        contors = imutils.grab_contours(contors)
        contmask = np.zeros(mask.shape, dtype="uint8") * 255

        for c in contors:
            if cv.contourArea(c) > 1000:
                cv.drawContours(contmask, [c], -1, (255, 255, 255), -1)

        mask = cv.bitwise_and(mask, contmask, mask=contmask)
        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)
        cv.imshow("mask", contmask)
        # display the green channel
        cv.imshow("green", mask)
        # reduce the size of the image by a factor of 2
        # convert to array
        array = np.array(mask)
        # resize the array by 50%
        resized = cv.resize(array, (0, 0), fx=0.5, fy=0.5)
        # predict the steering angle
        steering = model.predict(resized.reshape(1, 240, 320, 1))
        print(steering)
        sio.emit("steer", float(steering[0][0]))

        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    except:
        break

sio.wait()
