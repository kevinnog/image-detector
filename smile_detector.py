import cv2

face_detector = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('assets/haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)

while True:
    successfull_frame_read, frame = webcam.read()

    if not successfull_frame_read:
        break
        
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    faces = face_detector.detectMultiScale(grayscale_frame)

    for (x, y, w, h) in faces:
        the_face = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        the_face = frame[y:y+h, x:x+w]
        grayscale_face = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(grayscale_face, scaleFactor=1.7, minNeighbors=20)

        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (255, 0, 0), 2)
        
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    cv2.imshow('Why so serios', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()