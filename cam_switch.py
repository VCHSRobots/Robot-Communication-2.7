import socket
import cv2
import time
import numpy

capture = cv2.VideoCapture(0)
capture2 = cv2.VideoCapture(1)

def displayFrame1():
	while True: 
		ret, frame = capture.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame', )
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	capture.release()
	cv2.destroyAllWindows()

#def displayFrame2():
#	while True:
#		ret, frame = capture2.read()
#		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#		cv2.imshow('frame',gray)
#		if cv2.waitKey(1) & 0xFF == ord('q'):
#			break
#	capture2.release()
#	cv2.destroyAllWindows()

while True:
	displayFrame1()
