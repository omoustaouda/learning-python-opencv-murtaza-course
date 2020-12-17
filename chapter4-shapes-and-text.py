import cv2
import numpy as np

# Black image (0 -> black, 1 -> white)
img = np.zeros((512, 512, 3), np.uint8)

print('Image content: ' + str(img))

# BGR
# Square in the image
# img[200:300, 100:200] = 255, 0, 0

cv2.line(
    img,
    (0, 0),  # starting point
    (300, 300),  # ending point
    (0, 255, 0),  # color
    3  # thickness
)

cv2.rectangle(
    img,
    (0, 0),
    (250, 350),
    (0, 0, 255),
    # cv2.FILLED  # optional
)

cv2.circle(
    img,
    (400, 50),  # center
    30,  # radius
    (255, 255, 0),  # color
    5  # thickness
)

cv2.putText(
    img,
    'Hello dear!',
    (300, 200),
    cv2.FONT_ITALIC,
    1,
    (0, 150, 0),
    3
)

cv2.imshow('Image', img)

cv2.waitKey(0)
