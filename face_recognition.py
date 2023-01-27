# KRISNA SANTOSA - 04 January 2021
# Face Recognition with OpenCV and Python

import cv2
# algoritma haarcascade
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# kamera = cv2.VideoCapture(0)
kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW) # untuk OpenCV>=3.4
# Sizing kamera
kamera.set(3, 640)  # lebar itu kodenya 3,jadi saya atur lebar menjadi 640
kamera.set(4, 480)  # tinggi itu kodenya 4,jadi saya atur tinggi menjadi 480

# Membaca file algoritma haarcascade xml
# faceDetector = cv2.CascadeClassifier(
#     'face_recognition/haarcascade_frontalface_default.xml')
faceDetector = cv2.CascadeClassifier(
    './haarcascade_frontalface_default.xml')

while True:
    retV, frame = kamera.read()
    abuabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame,#scalefactor.
    faces = faceDetector.detectMultiScale(abuabu, 1.3, 5)
    # Membuat kotak x+w,y+h(x+lebar),(y+high)
    for(x, y, w, h) in faces:
        # warna disini bukan rgb tapi gbr
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    cv2.imshow('Webcam Krisna Santosa', frame)
    #cv2.imshow('Webcam Krisna Santosa ke2', abuabu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
