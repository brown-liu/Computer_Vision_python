import cv2
print("cv2 imported")
print(cv2.__version__)
import  time
img =cv2.imread('airplan.jpg')
# cv2.imshow("Aircraft",img)
# if waitKey(n) n =0 means will keep waiting, if n =1000 means wait for 1 second
# cv2.waitKey(1000)
cv2.destroyAllWindows()


# 0 means number 1 cam device on loca machine, can also replace to file name so can open some other video file
cap =cv2.VideoCapture(0)
# width    **********underneath two dont seems to work on MacOS
# cap.set(3,1300)
#height
# cap.set(4,1470)
# brightness
cap.set(10,200)
while True:
    start=time.time()
    operating,img=cap.read()
    cv2.imshow("video",img)
    print(f"FTP = {round(1/(time.time()-start),2)}")

    if cv2.waitKey(1)&0xFF ==ord('q'):
        break