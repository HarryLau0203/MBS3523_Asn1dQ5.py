import cv2
import numpy as np
print(cv2.__version__)

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('MBS3523')
cv2.createTrackbar('X_POS','MBS3523',640,640,nil)
cv2.createTrackbar('Y_POS','MBS3523',640,480,nil)

while True:
    success, img = cam.read()
    cv2.putText(img,'MBS3523 Assignment 1d-Q5 Name:Lau Chi Wing',(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.75,(225,135,10),3)
    x = cv2.getTrackbarPos('X_POS', 'MBS3523')
    y = cv2.getTrackbarPos('Y_POS', 'MBS3523')
    cv2.line(img,(x,0),(x,755),(255,0,0),2)
    cv2.line(img,(0,y),(750,y),(255,0,0),2)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
