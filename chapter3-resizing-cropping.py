import cv2
import numpy as np

img = cv2.imread('Resources/dragon-tree.jpg')
print('Original img shape: ' + str(img.shape))

# The height come first and then the width
imgResized = cv2.resize(img, (400, 300))
print('Resized img shape: ' + str(imgResized.shape))

# Same here: the height come first, followed by width
imgCropped = img[0:200, 200:500]

cv2.imshow('Original', img)
# cv2.imshow('Resized', imgResized)
cv2.imshow('Cropped', imgCropped)

cv2.waitKey(0)
