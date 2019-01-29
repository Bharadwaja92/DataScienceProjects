import cv2
import os
import numpy as np

# subjects = sorted(['PreetyZinta', 'ShahrukhKhan', 'SushmitaSen', 'Virat_Kohli', 'TomCruise'])
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

            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)

            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels


print("Preparing data...")

# print(os.listdir('../training_data'))
#
# import sys
# sys.exit(2)

faces, labels = prepare_training_data("../training_data")
print('labels are', labels)
print('subjectsDict is', subjectsDict)

print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img):
    img = test_img.copy()
    face, rect = detect_face(img)

    label, confidence = face_recognizer.predict(face)
    print('label, confidence is', label, confidence)
    # label_text = subjects[label]
    label_text = subjectsDict[label]

    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img


print("Predicting images...")

# test_img1 = cv2.imread("/home/saibharadwaj/Downloads/test1.jpg")
# predicted_img1 = predict(cv2.resize(test_img1, (400, 500)))
# cv2.imshow('predictedImage1', cv2.resize(predicted_img1, (400, 500)))

test_img2 = cv2.imread("/home/saibharadwaj/Downloads/test2.jpg")          # ok
predicted_img2 = predict(cv2.resize(test_img2, (400, 500)))
cv2.imshow('predictedImage2', cv2.resize(predicted_img2, (400, 500)))

# test_img3 = cv2.imread("/home/saibharadwaj/Downloads/test3.jpg")
# predicted_img3 = predict(cv2.resize(test_img3, (400, 500)))
# cv2.imshow('Predicted3', predicted_img3)

test_img4 = cv2.imread("/home/saibharadwaj/Downloads/test4.jpg")
predicted_img4 = predict(cv2.resize(test_img4, (400, 500)))
cv2.imshow('Predicted4', predicted_img4)

# test_img5 = cv2.imread("/home/saibharadwaj/Downloads/test5.jpg")          # Virat Kohli
test_img5 = cv2.imread("/home/saibharadwaj/Downloads/test5_1.jpeg")          # Virat Kohli
predicted_img5 = predict(cv2.resize(test_img5, (400, 500)))
cv2.imshow('Predicted5', predicted_img5)

# test_img6 = cv2.imread("/home/saibharadwaj/Downloads/test6.png")          # Ravi teja
# # predicted_img6 = predict(cv2.resize(test_img6, (400, 500)))
# predicted_img6 = predict(test_img6)
# cv2.imshow('Predicted6', predicted_img6)

test_img7 = cv2.imread("/home/saibharadwaj/Downloads/test7.jpg")          # Mehreen
predicted_img7 = predict(test_img7)
cv2.imshow('Predicted7', predicted_img7)

print("Prediction complete")

# display both images
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()





