#!/usr/bin/pyhton3

import cv2
#strating camera
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    #converting image frame into grey scale
    graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)
    #now we can drW ALL those patterens
    # #1 line
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)
    # #2 recrangle
    cv2.rectangle(frame,(50,50),(150,200),(0,0,250),2)
    # #3 circle
    cv2.circle(frame,(200,300),100,(13,44,123),2)
    # #4 text
    font=cv2.FONT_HERSHEY_SIMPLEX # this is font type
    cv2.putText(frame,"HOLA AMIGO",(413,276),font,2,(0,2,55),2,cv2.LINE_AA)
    #           frame_name,Text,    Staring, ,whole_fonr_width, font color,font_line_width 
    cv2.imshow('live',frame-75)
    #cv2.imshow('livegrey',graying)
    if cv2.waitKey(10) & 0xff == ord('q') : #0xff is to give some key value like keyboard input to quit camera
        break
#cv2.destroyWindows('live')
cv2.destroyAllWindows()#this will destroy all windows
# to close camera
cap.release()
