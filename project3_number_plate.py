import cv2
import numpy
import time

number_plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea=500
color = (255,0,0)
count =0
def runCam(count):

    cap=cv2.VideoCapture(0)
    global imgRoi
    while True:
        start=time.time()
        _, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = number_plate_cascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in faces:
            area=w*h
            if area>minArea:
                cv2.rectangle(img, (x, y), (x + w, y + h), (250, 0, 0), 2)
                cv2.putText(img,"Number Plate",(x,y-4),cv2.FONT_HERSHEY_PLAIN,1,color,2)
                imgRoi=img[y:y+h,x:x+w]
                cv2.imshow("Camera", imgRoi)
        cv2.imshow("Camera", img)
        print(f"FPS = {round(1/(time.time()-start),2)}")
        if cv2.waitKey(1)&0xff==ord('s'):
            cv2.imwrite(f"record{count}.jpg",imgRoi)
            cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
            cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
            cv2.imshow("Result",img)
            cv2.waitKey(500)
            count+=1
        if cv2.waitKey(1)&0xff==ord('q'):
            return

runCam(count)
cv2.destroyAllWindows()
