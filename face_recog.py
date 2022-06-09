import os
import cv2
import face_recognition

def face_rec(name:str):
    directory = 'images/'
    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f):
            basename = os.path.basename(f)
            (filename,ext) = os.path.splitext(basename)
            if filename == name:
                return 'Present'
    return 'Absent'

def compare_faces():
    img = cv2.imread("user1.jpg")
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    img2 = cv2.imread("user2.jpg")
    rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

    result = face_recognition.compare_faces([img_encoding], img_encoding2)
    return result[0]