import cv2

video = cv2.VideoCapture('video.mp4')

car_tracker = cv2.CascadeClassifier("assets/car_detector.xml")
pedestrians_tracker = cv2.CascadeClassifier("assets/pedestrians.xml")

while True:
    read_successful, frame = video.read()

    if read_successful:
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscale_frame)
    pedestrians = pedestrians_tracker.detectMultiScale(grayscale_frame)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Self Driving Car", frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()