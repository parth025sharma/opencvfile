#!/usr/bin/pyhton3

import cv2
#strating camera
cap=cv2.VideoCapture(0)
#addng plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# now saving video                 playback_speed_20   width,hight           
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))
#                       name_VIDEO,plugin,fps,resolutioin of camera


while cap.isOpened():
    status,frame=cap.read()     
    cv2.imshow('live',frame)
    # patterns can also be drawn
    output.write(frame) # sending data to VideoWrite
    #cv2.imshow('livegrey',graying)
    if cv2.waitKey(10) & 0xff == ord('q') : #0xff is to give some key value like keyboard input to quit camera
        break
#cv2.destroyWindows('live')
cv2.destroyAllWindows()#this will destroy all windows
# to close camera
cap.release()
