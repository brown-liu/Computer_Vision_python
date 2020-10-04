import cv2
import numpy as np

path="shape.jpg"
img=cv2.imread(path)

def get_contours(img):
    #src // retrivement method : many option, this one is good for outer contour //
    contours,Hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            print(area)
            cv2.drawContours(img_contor,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)


            if objCor==3: ObjectType="Triangle"
            elif objCor==4: ObjectType="Rectangle"
            elif objCor==5: ObjectType="Five sider"
            else: ObjectType='Not sure'

            cv2.rectangle(img_contor, (x, y), (x + w, y + h), (0, 155, 0), 2)
            cv2.putText(img_contor,ObjectType,(
                x+(w//2)-10,y+(h//2)-10),
            cv2.FONT_HERSHEY_PLAIN,1,(0,155,0),1)




img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),1)
img=cv2.resize(img,(800,600))
img_gray=cv2.resize(img_gray,(800,600))
img_blur=cv2.resize(img_blur,(800,600))
img_canny=cv2.Canny(img_blur,50,50)


img_t=np.hstack((img_gray,img_blur))

cv2.imshow("IMG",img)
# cv2.imshow("Gray",img_gray)
# cv2.imshow("Blur",img_blur)
# cv2.imshow('Stack',img_t)
# cv2.imshow("Canny",img_canny)

img_contor=img.copy()
get_contours(img_canny)
cv2.imshow("new",img_contor)

cv2.waitKey(0)