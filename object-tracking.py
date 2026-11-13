import cv2
import time
import math

video = cv2.VideoCapture("basquete.mp4")

tracker = cv2.TrackerCSRT_create()

returned, img = video.read()

bounding_box = cv2.selectROI("tracking",img, False)

tracker.init(img,bounding_box)

print(bounding_box)

def draw_box(img,bounding_box):
    x,y,w,h = int(bounding_box[0]),int(bounding_box[1]),int(bounding_box[2]),int(bounding_box[3])

    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,255),3,1 )

    cv2.putText(img, "rastreando",(75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0), 2)

while True:
    check, img = video.read()

    sucsses, bounding_box = tracker.update(img)

    if sucsses:
        draw_box(img, bounding_box)

    else:
        cv2.putText(img, "errou",(75,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255), 2)

    cv2.imshow("Resulatdo ", img)
    key = cv2.waitKey(25)
    if key ==  32:
        print("Interrompido")
        break
video.release()
cv2.destroyAllWindows()