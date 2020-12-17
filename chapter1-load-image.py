import cv2

print('OpenCV loaded!')

img = cv2.imread('Resources/dragon-tree.jpg')
cv2.imshow('My image windows', img)
cv2.waitKey(0)
