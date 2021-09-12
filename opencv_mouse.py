import cv2
import numpy as np
# import HandTrackingModule as htm
import mediapipe as mp
import time
import autopy

import threading

from WebcamVideoStream import WebcamVideoStream

##################
#wCam,hCam = 640,480


wCam,hCam = 320,240
margin = 75
adjVer = -30
adjHor = -10
smoothening = 5
plocX , plocY = 0 , 0
clocX , clocY = 0 , 0
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

wScr, hScr = autopy.screen.size()


def readFrame():
	global success, img, cap
	while True:
		success, img = cap.read()

threading.Thread(target = readFrame, args = ()).start()

while True:
	#success, img = cap.read()
	
	#imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	xmouse,ymouse = None,  None
	results = hands.process(img)#RGB)
	
	cv2.rectangle(img, (margin + adjHor,margin + adjVer), (wCam - margin + adjHor, hCam - margin + adjVer), (0xff,0xee,0), 1)
	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				h,w,c = img.shape
				cx,cy = int(lm.x *w), int(lm.y*h)
				if id == 8 or id == 12: #telunjuk dan jari tengah
					if id == 8 :
						#xmouse,ymouse = cx, cy
						xmouse = np.interp(cx,(margin + adjHor,wCam - margin + adjHor),(0,wScr))
						ymouse = np.interp(cy,(margin + adjVer,hCam - margin + adjVer),(0,hScr))
						
						# > menghaluskan pergerakan mouse
						#clocX = plocX + (xmouse - plocX) / smoothening
						#clocY = plocY + (ymouse - plocY) / smoothening
						
					cv2.circle(img, (cx,cy), 3, (0,0,255), cv2.FILLED)
				else:
					pass
					#cv2.circle(img, (cx,cy), 3, (0xff,0xee,0), cv2.FILLED)

			#mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
	
	#cTime = time.time()
	#fps = 1 / (cTime - pTime)
	#pTime = cTime
	
	# cv2.putText(img, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
	#cv2.putText(img,str(int(fps)), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255),1)
	if xmouse != None and ymouse != None:
		print("(",xmouse,",",ymouse,")")
		if (wScr-xmouse) > 0 and ymouse > 0 and (wScr-xmouse) < wScr and ymouse < hScr:
			autopy.mouse.move(wScr - xmouse,ymouse)
	
	cv2.imshow("Image",img)
	
	cv2.waitKey(1)


