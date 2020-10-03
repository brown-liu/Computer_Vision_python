import cv2
import numpy as np


img =np.zeros((512,512,3),np.uint8)

cv2.imshow("IMAGE",img)

img[:]= 255,0,0
print(img)
# createline src // start // end // color //thickness
cv2.line(img,(0,0),(512,512),(0,222,2),8)
# create rectrangle src // start(TL) // end(BR) // line width or can use cv2,FILL
cv2.rectangle(img,(20,40),(300,300),(0,0,255),2)
cv2.circle(img,(100,100),30,(33,33,33),5)

text ='i can put anything here'
cv2.putText(img,f"{text}",(300,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,150,150),2)

cv2.imshow("IMAGE_2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
