import cv2
import numpy as np
# import HandTrackingModule as htm
import mediapipe as mp
import time
import autopy

import threading

from WebcamVideoStream import WebcamVideoStream

##################
wCam,hCam = 640,480

##################

cap = cv2.VideoCapture(0)

cap.set(3,wCam)
cap.set(4,hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
					  max_num_hands=1,
					  min_detection_confidence=0.5,
					  min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
success, img = cap.read()

def readFrame():
	global success, img, cap
	while True:
		success, img = cap.read()

threading.Thread(target = readFrame, args = ()).start()

while True:
	#success, img = cap.read()
	
	#imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	results = hands.process(img)#RGB)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				h,w,c = img.shape
				cx,cy = int(lm.x *w), int(lm.y*h)
				cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)

			mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
	
	cTime = time.time()
	fps = 1 / (cTime - pTime)
	pTime = cTime
	
	# cv2.putText(img, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
	# cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,255),3)
	
	cv2.imshow("Frame",img)
	
	cv2.waitKey(1)


