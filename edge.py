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

		_, thresh = cv2.threshold(canny, 127, 255, 0)
		im2, contours, hir = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		cv2.drawContours(canny, contours, -1, (0, 255, 0), 3)

		cv2.imshow('cannyh', canny)

		cv2.imshow('im2', im2)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
 
cv2.destroyAllWindows()
 
#release the frame
cam.release()
