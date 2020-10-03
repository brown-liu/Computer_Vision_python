import cv2
import numpy as np

path="shape.jpg"
img=cv2.imread(path)

def get_contours(img):
    #src // retrivement method : many option, this one is good for outer contour //
    contours,Hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img,cnt,-1,(255,0,0),3)
        peri=cv2.arcLength(cnt,True)
        print(peri)


img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),1)
img=cv2.resize(img,(400,480))
img_gray=cv2.resize(img_gray,(400,480))
img_blur=cv2.resize(img_blur,(400,480))
img_canny=cv2.Canny(img_blur,50,50)


img_t=np.hstack((img_gray,img_blur))

cv2.imshow("IMG",img)
# cv2.imshow("Gray",img_gray)
# cv2.imshow("Blur",img_blur)
# cv2.imshow('Stack',img_t)
cv2.imshow("Canny",img_canny)

img_x=img_gray.copy()
get_contours(img_x)
cv2.imshow("new",img_x)

cv2.waitKey(0)