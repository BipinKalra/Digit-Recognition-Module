import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while 1:
    # Take each frame
    ret, frame = cam.read()

    if ret: 
        # Convert to HSV for simpler calculations
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
        canny = cv2.Canny(frame,100,200)
        
        cv2.imshow('cannyh', canny)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv2.destroyAllWindows()
 
#release the frame
cap.release()