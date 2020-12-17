import cv2
import numpy as np

img = cv2.imread('Resources/dragon-tree.jpg')

imgHorStack = np.hstack((img, img))
imgVerStack = np.vstack((img, img))

cv2.imshow('Horizontal stack', imgHorStack)
cv2.imshow('Vertical stack', imgVerStack)

cv2.waitKey(0)
