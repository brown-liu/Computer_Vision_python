import cv2
import time
import numpy as np

myColors=[[5,107,0,19,255,255],
          [133,56,0,159,156,255],
          [57,76,0,100,255,255]]

myColorValues=[
    [51,153,255],
    [255,0,255],
    [0,255,0]
]
cap =cv2.VideoCapture(0)

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count =0
    newPoints=[]
    for color in myColors:
        lower =np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(color[0]),mask)
        x,y = get_contours(mask)
        cv2.circle(img_final,(x,y),10,(255,0,0),cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints

def get_contours(img):
    #src // retrivement method : many option, this one is good for outer contour //
    contours,Hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        x,y,w,h=0,0,0,0
        if area>500:
            print(area)
            cv2.drawContours(img_final,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorVlaues):
    for point in myPoints:
        cv2.circle(img_final,(point[0],point[1]),10,myColorVlaues[point[2]],cv2.FILLED)

while True:
    start=time.time()
    operating,img=cap.read()
    img_final=img.copy()
    newPoints = findColor(img,myColors)
    if len(newPoints)!=0:
        for newP in newPoints:
            newPoints.append(newP)
    cv2.imshow("video", img_final)
    print(f"FTP = {round(1/(time.time()-start),2)}")
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
