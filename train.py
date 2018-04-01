import os
import cv2
import numpy as np
from PIL import Image

# cv2.face_LBPHFaceRecognizer

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'data/'


def getFace(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        face = np.array(faceImg, 'uint8')
        ID = int(imagePath.replace(path, "").split('.')[0])
        faces.append(face)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training", face)
        cv2.waitKey(100)
    return np.array(IDs), faces


def train():
    Ids, faces = getFace(path)

    recognizer.train(faces, Ids)
    recognizer.save('recognizer/trainingData.yml')
    cv2.destroyAllWindows()
