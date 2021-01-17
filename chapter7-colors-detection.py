from utils import stackImages
import cv2
import numpy as np


def empty(p):
    pass


img = cv2.imread('Resources/oud.jpg')
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

trackbarWinName = 'Trackbars'
cv2.namedWindow(trackbarWinName)
cv2.resizeWindow(trackbarWinName, 640, 240)
cv2.createTrackbar('Hue min', trackbarWinName, 11, 179, empty)
cv2.createTrackbar('Hue max', trackbarWinName, 37, 179, empty)
cv2.createTrackbar('Sat min', trackbarWinName, 20, 255, empty)
cv2.createTrackbar('Sat max', trackbarWinName, 207, 255, empty)
cv2.createTrackbar('Val min', trackbarWinName, 129, 255, empty)
cv2.createTrackbar('Val max', trackbarWinName, 255, 255, empty)

while True:
    hMin = cv2.getTrackbarPos('Hue min', trackbarWinName)
    hMax = cv2.getTrackbarPos('Hue max', trackbarWinName)
    sMin = cv2.getTrackbarPos('Sat min', trackbarWinName)
    sMax = cv2.getTrackbarPos('Sat max', trackbarWinName)
    vMin = cv2.getTrackbarPos('Val min', trackbarWinName)
    vMax = cv2.getTrackbarPos('Val max', trackbarWinName)

    lowerMatrix = np.array([hMin, sMin, vMin])
    upperMatrix = np.array([hMax, sMax, vMax])
    mask = cv2.inRange(imgHsv, lowerMatrix, upperMatrix)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # print(hMin, hMax, sMin, sMax, vMin, vMax)

    imgsStack = stackImages(
        0.6,
        (
            [img, imgHsv],
            [mask, imgResult]
        )
    )

    cv2.imshow('All imgs', imgsStack)

    cv2.waitKey(1)
