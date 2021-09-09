import cv2
import numpy as np
# import HandTrackingModule as htm
import time
import autopy

##################
wCam,hCam = 640,480

##################

cap = cv2.VideoCapture(0)

cap.set(3,wCam)
cap.set(4,hCam)

pTime = 0

while True:
	success, img = cap.read()
	
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	cTime = time.time()
	
	fps = 1 / (cTime - pTime)
	
	pTime = cTime
	
	cv2.putText(img, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
	
	cv2.imshow("Image",img)
	
	cv2.waitKey(1)


