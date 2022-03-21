#############################################################
# THIS CODE IS USED TO TEST THE IMAGE PROCESSING FUNCTIONS, #
#      THE MAIN FUNCTION IS TO MASK OFF THE LANE LINES      #
#       AND THEN RESIZE THE IMAGE TO A SMALLER SIZE.        #
#############################################################


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ip = "192.168.1.139"

# grab the image from ip address

cap = cv.VideoCapture("http://%s:8080/?action=stream" % ip)

while True:
    ret, frame = cap.read()
    cv.imshow("frame", frame)
    blur = cv.GaussianBlur(frame, (35, 35), 0)
    # isolate green channel
    cv.imshow("blur", blur)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    # isolate green channel
    mask = cv.inRange(hsv, (40, 0, 40), (90, 255, 240))
    mask = cv.GaussianBlur(mask, (5, 5), 0)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)
    mask = cv.GaussianBlur(mask, (5, 5), 0)
    # display the green channel
    cv.imshow("green", mask)
    # reduce the size of the image by a factor of 2
    # convert to array
    array = np.array(mask)
    # resize the array by 50%
    resized = cv.resize(array, (0, 0), fx=0.5, fy=0.5)

    cv.imshow("resized", resized)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
