import cv2
import time
#
# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# img=cv2.imread("tiananmen.jpg")
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces=face_cascade.detectMultiScale(imgGray,1.1,4)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)
#
#
# cv2.imshow("Tian An Men",img)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

def runCam():
    cap=cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        start=time.time()
        _, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (250, 0, 0), 2)

        cv2.imshow("Camera", img)
        print(f"FPS = {round(1/(time.time()-start),2)}")
        if cv2.waitKey(1)&0xff==ord('q'):
            return


runCam()
cv2.destroyAllWindows()

