
import cv2
import numpy as np

def preProcessing(frame):
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img_blur=cv2.GaussianBlur(img_gray,(5,5),1)
    img_canny=cv2.Canny(img_blur,200,200)
    kernel=np.ones((5,5))
    img_dial=cv2.dilate(img_canny,kernel,iterations=2)
    img_Thres=cv2.erode(img_dial,kernel,iterations=1)
    return  img_Thres


def getContour(img):
    biggest=np.array([])
    maxArea=0
    contour , hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        print(f"  {'*'*20} AREA = {area}{'*'*20}")
        if area>3000:
            cv2.drawContours(final,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02 * peri,True)
            if area>maxArea and len(approx)==4:
                biggest=approx
                maxArea=area
    return biggest

def getWarp(img,biggest):
    pass



if __name__=="__main__":
    cap=cv2.VideoCapture(0)
    while True:

        success,frame = cap.read()
        frame=cv2.resize(frame,(640,400))
        final=frame.copy()

        imgThr=preProcessing(frame)
        biggest = getContour(imgThr)
        getWarp(frame, biggest)

        cv2.imshow("Video",imgThr)
        cv2.imshow("Video_Final", final)

        if cv2.waitKey(1)& 0xFF==ord("q"):
            break
    cv2.destroyAllWindows()