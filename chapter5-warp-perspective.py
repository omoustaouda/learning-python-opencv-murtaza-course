import cv2
import numpy as np

img = cv2.imread('Resources/books-pile.jpg')
width, height = 250, 400

ptsOriginalImg = np.float32([
    [230, 185],  # top left
    [390, 88],   # top right
    [655, 296],  # bottom left
    [791, 176],  # bottom right
])
ptsMapping = np.float32([
    [0, 0],  # top left
    [width, 0],   # top right
    [0, height],  # bottom left
    [width, height]  # bottom right
])

matrixTransformation = cv2.getPerspectiveTransform(ptsOriginalImg, ptsMapping)
imgBook = cv2.warpPerspective(img, matrixTransformation, (width, height))

cv2.imshow('Original', img)
cv2.imshow('Book perspective aligned', imgBook)

cv2.waitKey(0)
