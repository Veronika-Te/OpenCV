import cv2 as cv
from matplotlib import pyplot as plt

img_grayscale=cv.imread('media/geometric.jpg', 0) #cv.IMREAD_GRAYSCALE) #0
img_color=cv.imread('media/geometric.jpg', cv.IMREAD_COLOR) #1
img_unchanged=cv.imread('media/geometric.jpg', cv.IMREAD_UNCHANGED) #-1

# cv.imshow('Grayscale image', img_grayscale)
# cv.imshow('Colored image', img_color)
# cv.imshow('Unchanged image', img_unchanged)
plt.subplot(231),plt.imshow(cv.cvtColor(img_grayscale,cv.COLOR_BGR2RGB)) #BGR
plt.subplot(233),plt.imshow(cv.cvtColor(img_color,cv.COLOR_BGR2RGB))
plt.subplot(234),plt.imshow(cv.cvtColor(img_unchanged,cv.COLOR_BGR2RGB)) 
#plt.imshow(img_grayscale) #RGB
#plt.axis("off")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('grayscaled_geometric.jpg',img_grayscale)