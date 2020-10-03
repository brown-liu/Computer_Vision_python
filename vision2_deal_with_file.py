import cv2
import numpy as np
import time
img=cv2.imread("airplan.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''src is the source, original or input image in the form of numpy array
dsize is the desired size of the output image, given as tuple
fx is the scaling factor along X-axis or Horizontal axis
fy is the scaling factor along Y-axis or Vertical axis
interpolation could be one of the following values.
INTER_NEAREST
INTER_LINEAR
INTER_AREA
INTER_CUBIC
INTER_LANCZOS4'''

img_gray = cv2.resize(img_gray,(800,600))
img_blur=cv2.GaussianBlur(img_gray,(7,7),0)

# src followed by hi-threshold and lo -threshold
img_canny_v1=cv2.Canny(img_gray,50,100)
img_canny_v2=cv2.Canny(img_gray,150,200)
img_canny_v3 = cv2.Canny(img_gray,300,1000)

kernel_1=np.ones((5,5),dtype=np.uint8)
kernel_2=np.ones((10,10),dtype=np.uint8)

img_dialation_V1 =cv2.dilate(img_gray,kernel=kernel_1,iterations=1)
img_dialation_V2 =cv2.dilate(img_gray,kernel=kernel_1,iterations=6)
img_dialation_V3 =cv2.dilate(img_gray,kernel=kernel_2,iterations=1)

img_Eroded = cv2.erode(img_dialation_V1,kernel_1,iterations=1)

cv2.imshow("Blur",img_blur)
cv2.imshow("IMG",img_gray)
cv2.imshow("Canny_v1",img_canny_v1)
cv2.imshow("Canny_V2",img_canny_v2)
cv2.imshow("Canny_V3",img_canny_v3)
cv2.imshow("Dialation_V1",img_dialation_V1)
cv2.imshow("Dialation_V2",img_dialation_V2)
cv2.imshow("Dialation_V3",img_dialation_V3)
cv2.imshow("Eroded",img_Eroded)


cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.waitKey(0)
# cv2.destroyAllWindows()