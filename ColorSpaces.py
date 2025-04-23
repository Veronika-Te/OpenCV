import cv2 as cv
import numpy as np

bright = cv.imread('media/indoor.jpg')
dark = cv.imread('media/outdoor.jpg')

#The LAB Color-Space
brightLAB = cv.cvtColor(bright, cv.COLOR_BGR2LAB)
darkLAB = cv.cvtColor(dark, cv.COLOR_BGR2LAB)

# The YCrCb Color-Space
brightYCB = cv.cvtColor(bright, cv.COLOR_BGR2YCrCb)
darkYCB = cv.cvtColor(dark, cv.COLOR_BGR2YCrCb)

# The HSV Color Space
brightHSV = cv.cvtColor(bright, cv.COLOR_BGR2HSV)
darkHSV = cv.cvtColor(dark, cv.COLOR_BGR2HSV)


# Extracting only the L channel (lightness) for visualizing the LAB Color-Space
brightL = brightLAB[:, :, 0]
darkL = darkLAB[:, :, 0]

cv.imshow('Bright L', brightL)
cv.imshow('Dark L', darkL)
cv.waitKey(0)
cv.destroyAllWindows()



## cv.imshow('Bright Image', brightLAB)
# cv.imshow('Dark Image', darkLAB)
# #cv.imshow('Image', brightLAB)
# cv.waitKey(0)
# cv.destroyAllWindows()


