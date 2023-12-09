#! /usr/bin/env python3

import cv2
import time
import datetime

vid_capture = cv2.VideoCapture(0)
facial_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
#number_plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")s

detection = False
detection_stopped_time = None
timer_started = False
sec_rec_after_detection = 5

frame_size = (int(vid_capture.get(3)), int(vid_capture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#out = cv2.VideoWriter("output.mp4", fourcc, 15.0, frame_size)

while True:
    _, frame = vid_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facial_cascade.detectMultiScale(gray, 1.3, 4)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 4)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False

        else:
            detection= True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 15.0, frame_size)
            print("Recording Started!")

    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= sec_rec_after_detection:
                detection = False
                timer_started = False
                out.release()
                print("Recording Stopped!")
        else:
            timer_started = True
            detection_stopped_time = time.time()



    if detection:
        out.write(frame)

    #DRAWING
    # for (x, y, width, height) in bodies:
    #     cv2.rectangle(frame, (x, y),(x + width, y + height), (50, 205, 50), 3)
    # for (x, y, width, height) in faces:
    #     cv2.rectangle(frame, (x, y),(x + width, y + height), (50, 205, 50), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

out.release()
vid_capture.release()
cv2.destroyAllWindows()
