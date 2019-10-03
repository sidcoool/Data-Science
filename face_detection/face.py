import cv2

capture=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
	ret,frame = capture.read()

	if ret==False:
		continue

	faces=face_cascade.detectMultiScale(frame,1.3,5)
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(100,0,255),2)
		#eyeframe=gray[y:y+h,x:x+h]
		eyecolor=frame[y:y+h,x:x+h]
		eyes=eye_cascade.detectMultiScale(eyecolor,1.03,3)
		for (x1,y1,w1,h1) in eyes:
			cv2.rectangle(eyecolor,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
    
	cv2.imshow('face detection',frame)

	key_pressed=cv2.waitKey(1)&0XFF
	if(key_pressed==ord('e')):
		break

capture.release()
cv2.destroyAllWindows()