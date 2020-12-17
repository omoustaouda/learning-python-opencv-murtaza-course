import cv2

print('OpenCV loaded!')

cap = cv2.VideoCapture('Resources/bigbunny.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('My video windows', img)
    # We check if the 'q' key has been pressed, if yes we quit the loop.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        pass
