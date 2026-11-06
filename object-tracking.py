import cv2
import time
import math

video = cv2.VideoCapture("basquete.mp4")

while True:
    check, img = video.read()

    cv2.imshow("Resulatdo ", img)
    key = cv2.waitKey(25)
    if key ==  32:
        print("Interrompido")
        break
video.release()
cv2.destroyAllWindows()