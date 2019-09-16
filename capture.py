import cv2, time



#Create an object. Zero for external camera
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 0
while True:
	a = a+ 1
	#create a frame object
	check, frame = video.read()

	print(check)
	print(frame)#repersenting an image

	#coverting to grayscale
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#Show the frame
	cv2.imshow("Capturing", gray)
	
	# For Playing
	key=cv2.waitKey(1)
	
	if key == ord('q'):
		break
		
		
	# For press any key to out (milliseconds)
	# cv2.waitKey(0)
	
print(a)
#shutdown camera
video.release()



#cv2.destroyAllWindows()
 