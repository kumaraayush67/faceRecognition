# Face Recognition

Aplication to Detects and Recognize faces in Python with opencv.

Opencv [haarcascade](https://github.com/opencv/opencv/tree/master/data/haarcascades) is being used for face detection.
Local Binary Patterns Histograms or [LBPHFaceRecognizer](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html) is being used for face recognition.

## Working

#### Face Detector

    * Takes the Face Id as Input.
    * Click Photos (Total 5 photos Required).
    * Detects the Face in the Picture. ( Using Haar Cascade )
    * Save it in the Directory.

#### Trainer

    * Search all the Photos saved in the directory.
    * Train on the photos and create trainingData.yml file.

#### Identifying faces

    * Reads trainingData.yml file
    * Predict/Identify Faces in a Video. ( Using LBPH Face Recognizer )

### Requirements

  * Python 3.3+
  * opencv-contrib-python 3.4.0.12
  * numpy 1.14.0
  * Pillow 5.0.0

### Todos

  * Create a Database and link it with faceId.

