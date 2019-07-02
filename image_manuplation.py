#!/usr/bin/python3

import cv2
img1=cv2.imread("pimg1.jpg")
img2=cv2.imread("pimg2.jpg")
#cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)
while 1<2:
    dif=cv2.absdiff(img1,img2)
    add=cv2.add(img1,img2)
    cv2.imshow("addtion",add)
    cv2.imshow("dif",dif)
    if cv2.waitKey(10) & 0xff==ord("q"):
        break
cv2.destroyAllWindows()

