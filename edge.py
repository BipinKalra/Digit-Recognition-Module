import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while 1:
	# Take each frame
	ret, frame = cam.read()

	if ret: 
		# Convert to HSV for simpler calculations
		imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		imgray = cv2.GaussianBlur(imgray, (5, 5), 0)

		canny = cv2.Canny(frame,100,200)

		# canny = cv2.bitwise_not(canny)


		ret,thresh = cv2.threshold(canny,127,255,0)
		im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		# print(type(contours))
		# print(len(contours))
		if len(contours):
			print("yo yo ")
			print(contours[0])
			print(contours[1])


		cropped = []

		for contour in contours:
			min_x, min_y, max_x, max_y = 10000000, 10000000, -1, -1
			for point in contour:
				point = point.flatten()

				x, y = point[:2]

				if x < min_x:
					min_x = x
				if x > max_x:
					max_x = x

				if y < min_y:
					min_y = y
				if y > max_y:
					max_y = y

			cropped.append(imgray[min_x:max_x, min_y:max_y])

		height, width = cropped[-1].shape[:2]
		if height > 0 and width > 0:
			cv2.imshow('cropped', cropped[-1])

		# arr = 

		cv2.drawContours(imgray, contours, -1, (0,255,0), 3)

		cv2.imshow('gray', imgray)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
 
cv2.destroyAllWindows()
 
#release the frame
cam.release()
