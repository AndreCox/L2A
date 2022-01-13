import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# open a video stream from the webcam
cap = cv.VideoCapture(0)


def canny(image):
    # convert to grayscale
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # blur the image
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # find edges
    canny = cv.Canny(blur, 50, 150)
    return canny


# display the video stream
while True:
    # find all green objects in the video stream and return the coordinates of the bounding boxes
    ret, frame = cap.read()
    # display the video stream
    cv.imshow("frame", frame)
    cv.imshow("canny", canny(frame))

    # quit the program when the user presses 'q'
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
