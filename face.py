# Import di vari moduli
import os
import numpy as np
import array
import cv2

# Haar Feature-based Cascade Classifier. Utilizziamo il template per la face recognition haarcascade_frontalface_default.xml. Lo trovate sul repo di Github di OpenCV
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Catturiamo streaming da /dev/video0
cap = cv2.VideoCapture(0)

# Impostazione della risoluzione... Naturalmente va aumentata.
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 240);
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 180);

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# Per ogni volto riconosciuto...
	for (x,y,w,h) in faces:
		img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
		# Esecuzione script bash per invio messaggi su HipChat
		time.sleep(3)
		os.system("bash send_message.sh")
                print "allarme inviato"
		exit()
	# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
