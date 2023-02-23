import numpy as np
import cv2
import beautiful_frames as bf

faceCascade = cv2.CascadeClassifier('path to haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,               #
        scaleFactor=1.2,    #
        minNeighbors=5,     #
        minSize=(30, 30)    #
    )

    for (x, y, w, h) in faces:
        bf.settings(20,255,10,2)
        img=bf.frame(img,x,y,w,h)
        
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:  # Esc key
        break
cap.release()
cv2.destroyAllWindows()
