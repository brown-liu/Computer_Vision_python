import cv2
import numpy as np


img=cv2.imread("lambo.webp")
new_h=np.hstack(([img,img,img,img]))
new_v=np.vstack((img,img))

# cv2.imshow("new",new_h)
# cv2.imshow("V",new_v)
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 700, 240)
def pp(val):
    pass
h_min = cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, pp)
h_max = cv2.createTrackbar("Hue Max", "TrackBars", 0, 179, pp)
s_min = cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, pp)
s_max = cv2.createTrackbar("Sat Max", "TrackBars", 0, 255, pp)
v_min = cv2.createTrackbar("Val Min", "TrackBars", 0, 255, pp)
v_max = cv2.createTrackbar("Val Max", "TrackBars", 0, 255, pp)


img=cv2.imread("lambo.webp")

while True:


    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    upper=np.array([h_max,s_max,v_max])
    lower = np.array([h_min,s_min,v_min])
    mask=cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Mask",mask)
    cv2.imshow("New2",imgHSV)

    if cv2.waitKey(0)&0xFF==ord("q"):
        break
cv2.destroyAllWindows()