import cv2
import numpy as np


def capture():
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    id = input('\n\nEnter Id : ')
    samNo = 0
    color = (255, 0, 0)
    cap = cv2.VideoCapture(0)
    while True:
        color = (255, 0, 0)
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        elif k == 13:
            color = (0, 255, 0)
            cv2.imwrite('data/' + str(id) + '.' + str(samNo) + '.jpg', gray[y:y + h, x:x + w])
            samNo += 1

        if samNo >= 5:
            break

    cap.release()
    cv2.destroyAllWindows()
