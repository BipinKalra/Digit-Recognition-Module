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

		blur = cv2.GaussianBlur(canny, (41, 41), 0)

		(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)

		image = frame.copy()

		roi=image[maxLoc[1]-250:maxLoc[1]+250,maxLoc[0]-250:maxLoc[0]+250,2:2]
			
		cv2.imshow('cannyh', canny)

		cv2.imshow('roi', roi)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
 
cv2.destroyAllWindows()
 
#release the frame
cam.release()
