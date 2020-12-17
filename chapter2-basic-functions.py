import cv2
import numpy as np

print('OpenCV loaded!')

img = cv2.imread('Resources/dragon-tree.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)

kernel = np.ones((5, 5), np.uint8)
imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilated, kernel, iterations=1)

cv2.imshow('Gray image', imgGray)
# cv2.imshow('Blurred image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dilated image', imgDilated)
cv2.imshow('Eroded image', imgEroded)
cv2.waitKey(0)
