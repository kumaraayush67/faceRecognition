import cv2
import numpy as np


def detectFace():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainingData.yml')
    id = 0

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(id), (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
