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


def green(image):
    # define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    # blur the image
    blur = cv.GaussianBlur(image, (9, 9), 0)
    # convert to HSV
    hsv = cv.cvtColor(blur, cv.COLOR_RGB2HSV)
    # create a mask
    mask = cv.inRange(hsv, lower_green, upper_green)
    return mask


# Change thresholds
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByColor = False
params.filterByArea = True
params.minArea = 100
params.maxArea = 1000
# helloworld


# display the video stream
while True:
    # find all green objects in the video stream and return the coordinates of the bounding boxes
    ret, frame = cap.read()
    # display the video stream
    cv.imshow("frame", frame)
    cv.imshow("canny", canny(frame))
    cv.imshow("green", green(frame))
    cv.imshow("green_canny", cv.bitwise_and(canny(frame), green(frame)))

    # quit the program when the user presses 'q'
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
        
