import numpy as np
import cv2
import datetime
import time
from threading import Thread

def capVid(name):
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    fourcc = cv2.VideoWriter_fourcc(*'X264')
    out = cv2.VideoWriter(f'flask\\static\\vid\\{name}.mp4', fourcc, 30, (640, 480))

    i = 0
    while(cap.isOpened()):
        i += 1
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if i > 30*60*5:
                break
        else:
            break
    cap.release()
    out.release()

def capVid1(name):
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(f'flask\\static\\vid\\{name}.avi', fourcc, 20.0, (640, 480))

    i = 0
    while(cap.isOpened()):
        i += 1
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if i > 40:
                break
        else:
            break
    cap.release()
    out.release()


while True:
    capVid(datetime.datetime.now().strftime('%H.%M_%d.%m.%Y'))

t1 = Thread(target=capVid, args=[datetime.datetime.now().strftime('%H.%M_%d.%m.%Y')])
t1.start()
