from WebcamVideoStream import *
from FPS import *

import time


#vs = WebcamVideoStream(src=0).start()
#vs.stream.set(3,640)
#vs.stream.set(4,480)

#fps = FPS().start()

#while True:
#	frame = vs.read()
#	cv2.imshow("Image",frame)
#	cv2.waitKey(1)

		
##################
wCam,hCam = 640,480

##################

# global cap 
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

# global grabbed, frame
grabbed, frame = cap.read()

def updateStream():
	global grabbed, frame, cap
	print("thread 1")
	while True:
		(grabbed,frame) = cap.read()
	print("updateStream")
		
def main():
	global grabbed, frame, cap
	cTime = 0
	pTime = 0
	while True:
		grabbed, frame = cap.read()
		cTime = time.time()
		fps = 1 / (cTime - pTime)
		pTime = cTime
		#fps.stop()
	#	#fps.update()
		cv2.putText(frame, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,127,0),2)
		cv2.imshow("Frame",frame)
		cv2.waitKey(1)
		
if __name__ == "__main__":

	task1 = Thread(target=main, args=())
	task1.start()
	
	#task2 = Thread(target=updateStream, args=())	
	#task2.start()








	
