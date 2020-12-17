import cv2
from cv2.cv2 import CAP_PROP_BRIGHTNESS, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH

print('OpenCV loaded!')

cameraId = 0

cap = cv2.VideoCapture(cameraId)

cap.set(CAP_PROP_FRAME_WIDTH, 640)
cap.set(CAP_PROP_FRAME_HEIGHT, 480)
# Camera brightness adjustments
cap.set(CAP_PROP_BRIGHTNESS, 166)

while True:
    success, img = cap.read()
    cv2.imshow('My lovely camera window', img)
    # We check if the 'q' key has been pressed, if yes we quit the loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
