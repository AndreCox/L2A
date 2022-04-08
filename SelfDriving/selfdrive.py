from cv2 import imshow
import keras as ks
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv
import socketio
from keras.preprocessing.image import img_to_array
import imutils



ip = "192.168.1.59"


# Load the model
model = ks.models.load_model("atlas4.h5")

# display stream from ip camera
cap = cv.VideoCapture("http://%s:8080/?action=stream" % ip)
# connecting to the PiCar
sio = socketio.Client()
sio.connect("http://%s:3000" % ip)

car_tilt = 45
sio.emit("tilt", car_tilt)


car_speed = 0
sio.emit("drive", car_speed)

car_pan = 90
sio.emit("pan", car_pan)

h_lower = 40
s_lower = 20
v_lower = 40

h_upper = 100
s_upper = 255
v_upper = 250

contor_area = 0

def null(x):
    pass

# display the captured frame
cv.namedWindow("Adjustments")
# set window size
cv.resizeWindow("Adjustments", 680, 680)
cv.createTrackbar("h_lower", "Adjustments", 40, 255, null)
cv.createTrackbar("s_lower", "Adjustments", 20, 255, null)
cv.createTrackbar("v_lower", "Adjustments", 40, 255, null)
cv.createTrackbar("h_upper", "Adjustments", 100, 255, null)
cv.createTrackbar("s_upper", "Adjustments", 255, 255, null)
cv.createTrackbar("v_upper", "Adjustments", 250, 255, null)

#cv.createTrackbar("Blur", "Adjustments", 5, 20, null)
cv.createTrackbar("Contour Area", "Adjustments", 0, 10000, null)


cv.createTrackbar("Car Speed", "Adjustments", 0, 100, null)
cv.createTrackbar("Car Tilt", "Adjustments", 45, 90, null)
cv.createTrackbar("Car Pan", "Adjustments", 90, 180, null)

while True:
    try:
        if (car_speed != cv.getTrackbarPos("Car Speed", "Adjustments")):
            car_speed = cv.getTrackbarPos("Car Speed", "Adjustments")
            sio.emit("drive", car_speed)

        if (car_tilt != cv.getTrackbarPos("Car Tilt", "Adjustments")):
            car_tilt = cv.getTrackbarPos("Car Tilt", "Adjustments")
            sio.emit("tilt", car_tilt)

        if (car_pan != cv.getTrackbarPos("Car Pan", "Adjustments")):
            car_pan = cv.getTrackbarPos("Car Pan", "Adjustments")
            sio.emit("pan", car_pan)

        h_lower = cv.getTrackbarPos("h_lower", "Adjustments")
        s_lower = cv.getTrackbarPos("s_lower", "Adjustments")
        v_lower = cv.getTrackbarPos("v_lower", "Adjustments")

        h_upper = cv.getTrackbarPos("h_upper", "Adjustments")
        s_upper = cv.getTrackbarPos("s_upper", "Adjustments")
        v_upper = cv.getTrackbarPos("v_upper", "Adjustments")

        contor_area = cv.getTrackbarPos("Contour Area", "Adjustments")






        ret, frame = cap.read()
        imshow("Frame", frame)
        blur = cv.GaussianBlur(frame, (5, 5), 0)
        hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
        # isolate green channel
        mask = cv.inRange(hsv, (h_lower, s_lower, v_lower), (h_upper, s_upper, v_upper))
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
            if cv.contourArea(c) > contor_area:
                cv.drawContours(contmask, [c], -1, (255, 255, 255), -1)

        # mix the contour mask with the mask 50%
        mask = cv.bitwise_and(mask, contmask)
        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)
        mask = cv.GaussianBlur(mask, (5, 5), 0)

        
        cv.imshow("mask", mask)
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
