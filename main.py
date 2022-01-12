import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#open a video stream from the webcam
cap = cv.VideoCapture(0)

params = cv.SimpleBlobDetector_Params()

# Change thresholds
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByColor = False
params.filterByArea = True
params.minArea = 100
params.maxArea = 1000


#display the video stream
while True:
    #find all green objects in the video stream and return the coordinates of the bounding boxes
    ret, frame = cap.read()
    lower_green = np.array([20 ,100, 20])
    upper_green = np.array([100,255,100])
    hst = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hst, lower_green, upper_green)
    mask_inv = cv.bitwise_not(mask)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.imshow('Video', cap.read()[1])
    
    #run blob detection on the mask and circle the detected blobs
    blobs = cv.SimpleBlobDetector_create(params)
    keypoints = blobs.detect(mask_inv)
    im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow('keypoints', im_with_keypoints)

    #quit the program when the user presses 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

