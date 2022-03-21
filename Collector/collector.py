import cv2 as cv
import numpy as np

# import keras
import socketio
import csv
from os import path

ip = "192.168.1.139"

if path.exists("frames/data.csv"):
    csvfile = "frames/data.csv"
    print("CSV file already exists resuming ")
    with open(csvfile, "a") as fp:
        wr = csv.writer(fp, dialect="excel")

else:
    csvfile = "frames/data.csv"
    print("CSV file does not exist creating one now ")
    with open(csvfile, "a") as fp:
        wr = csv.writer(fp, dialect="excel")
        wr.writerow(["steering"])

# display stream from ip camera
cap = cv.VideoCapture("http://%s:8080/?action=stream" % ip)
# connecting to the PiCar
sio = socketio.Client()
sio.connect("http://%s:3000" % ip)

steeringdata = 90


@sio.event
def steering(data):
    global steeringdata
    print(data)
    steeringdata = data


counter = 0
# display the captured frame
while True:
    ret, frame = cap.read()
    cv.imshow("frame", frame)
    # save a frame every second
    if (0) == 0:
        cv.imwrite("frames/" + str(int(counter)) + ".jpg", frame)

        with open("frames/data.csv", "a", encoding="UTF8", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", lineterminator="\n")
            writer.writerow([steeringdata])
    counter += 1
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

sio.wait()
