import time
import imutils
from imutils.video import FileVideoStream
import cv2
import os
import numpy as np

videoStream = '/home/saibharadwaj/Downloads/Mobius/DAI_C/AdVideos/Jiya_Jale-Dil_Se.MP4'
vs = FileVideoStream(videoStream).start()
time.sleep(1.0)
subjectsDict = {}

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    xmlFile = '/home/saibharadwaj/PycharmProjects/DSP/FaceRecognition/training_data/lbpcascade_frontalface.xml'
    xmlFile = '/home/saibharadwaj/PycharmProjects/DSP/FaceRecognition/training_data/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(xmlFile)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = [v for v in os.listdir(data_folder_path) if v.find('.') == -1]

    faces = []
    labels = []
    fg = 0

    for dir_name in dirs:
        print('Now looking at', dir_name,' folder')
        subjectsDict[fg] = dir_name
        label = fg
        fg += 1

        subject_dir_path = data_folder_path + "/" + dir_name

        subject_images_names = os.listdir(subject_dir_path)

        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;

            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)
            image = cv2.resize(image, (400, 500))

            # cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            # cv2.waitKey(100)

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels


print("Preparing data...")

faces, labels = prepare_training_data("training_data")
print('labels are', labels)
print('subjectsDict is', subjectsDict)

print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer = cv2.face.EigenFaceRecognizer_create()
# face_recognizer = cv2.face.FisherFaceRecognizer_create()

face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img):
    test_img = cv2.resize(test_img, (400, 500))
    img = test_img.copy()
    face, rect = detect_face(img)

    # print('Face is', face)
    if face is None:
        return test_img

    label, confidence = face_recognizer.predict(face)
    print('label, confidence is', label, confidence)
    label_text = subjectsDict[label]

    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img


while True and vs.more():
    frame = vs.read()
    frame = imutils.resize(image=frame)
    # predicted = predict(cv2.resize(frame, (400, 500)))
    predicted = predict(frame)
    # print('>>>', predicted)
    cv2.imshow('Predicted Video', predicted)
    print('frame is', frame)
    # cv2.imshow('frame', frame)
    cv2.waitKey(50)

# test_img1 = cv2.imread("/home/saibharadwaj/Downloads/test1.jpg")
# predicted_img1 = predict(cv2.resize(test_img1, (400, 500)))
# cv2.imshow('predictedImage1', cv2.resize(predicted_img1, (400, 500)))

cv2.waitKey(0)
cv2.destroyAllWindows()



