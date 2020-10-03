import cv2



img=cv2.imread("lambo.webp")
img_resized=cv2.resize(img,(300,200))


#height first and then width
img_crop=img[0:300,200:600]


cv2.imshow("lambo",img)
cv2.imshow("smaller",img_resized)
cv2.imshow("croped",img_crop)

print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()