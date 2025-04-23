import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os 

def read_image(path):
  """Read an image"""
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 1)
  cv.imshow('Image', image)
  cv.waitKey(0)
  cv.destroyAllWindows()
  return image

#Blur
def blur_img(image: np.ndarray):
  """Blur an image using the normalized box filter."""
  if image is None or not isinstance(image, np.ndarray):
    return
  ksize = (10, 10) 
  image = cv.blur(image, ksize)  
  cv.imshow('Blur', image)
  cv.waitKey(0)
  cv.destroyAllWindows()

def median_blur(image: np.ndarray):
  """Applying Median Blurring"""
  if image is None or not isinstance(image, np.ndarray):
    return
  median_image=cv.medianBlur(image, ksize=3)
  cv.imshow('Median Blur', median_image)
  cv.waitKey(0)
  cv.destroyAllWindows()

def gaussian_blur(image: np.ndarray):
  """Applying Gaussian Blurring"""
  if image is None or not isinstance(image, np.ndarray):
    return
  gaussian_blur = cv.GaussianBlur(src=image, ksize=(5,5),sigmaX=0, sigmaY=0)
  plt.subplot(121),plt.imshow(image),plt.title('Original')
  plt.subplot(122),plt.imshow(gaussian_blur),plt.title('Gaussian Blur')
  plt.show()
  cv.waitKey(0)
  cv.destroyAllWindows()


def bilateral_filter(image: np.ndarray):
  """Applying Bilateral Filtering"""
  if image is None or not isinstance(image, np.ndarray):
    return
  # Apply bilateral filter with d = 15,  
  # sigmaColor = sigmaSpace = 75. 
  bilateral=cv.bilateralFilter(image, 15,75,75)
  cv.imshow('Bilateral Filter', bilateral)
  cv.waitKey(0)
  cv.destroyAllWindows()

#Filter 2D
def apply_kernel(image: np.ndarray):
  if image is None or not isinstance(image, np.ndarray):
    return
  #for experiments
  kernel1=np.array([[0,0,0],[0,1,0],[0,0,0]]) #identity kernel
  #kernel2 = np.ones((5, 5), np.float32) / 25
  identity=cv.filter2D(src=image, ddepth=-1,kernel=kernel1)
  cv.imshow('Filtered 2D applying Kernel', identity)
  cv.waitKey(0)
  cv.destroyAllWindows()

#Filter 2D for sharpening
def sharpening(image: np.ndarray):
  """Sharpening the image"""
  if image is None or not isinstance(image, np.ndarray):
    return
  kernel3 = np.array([[0, -1,  0],
                      [-1,  5, -1],
                      [0, -1,  0]])
  sharp_img=cv.filter2D(src=image, ddepth=-1, kernel=kernel3)
  cv.imshow('Filtered 2D: Sharpening', sharp_img)
  cv.waitKey(0)

def create_kernels():
  """Creates different kernels as an examples"""
  kernel_rect = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
  kernel_cross = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
  kernel_ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

  print("RECT:\n", kernel_rect)
  print("CROSS:\n", kernel_cross)
  print("ELLIPSE:\n", kernel_ellipse)

def erode_dilate_image(image: np.ndarray):
  """Morphological operations"""
  if image is None or not isinstance(image, np.ndarray):
    return
  #Creating kernel 
  kernel = np.ones((5, 5), np.uint8) 
  # Using cv2.erode method, then dilate  
  
  #Erodes away the boundaries of the foreground object
  #image = cv.erode(image, kernel)
  img_erosion = cv.erode(image, kernel, iterations=1) 
  #Increases the object area, used to accentuate features
  img_dilation = cv.dilate(image, kernel, iterations=1) 
  
  plt.subplot(121),plt.imshow(img_erosion),plt.title('Erosion')
  plt.subplot(122),plt.imshow(img_dilation),plt.title('Dilation')
  plt.show()
  cv.waitKey(0)
  cv.destroyAllWindows()

def main():
  path='media/photo.png'
  img=read_image(path)
  median_blur(img)
  gaussian_blur(img)
  bilateral_filter(img)
  apply_kernel(img)
  erode_dilate_image(img)
  sharpening(img)
  create_kernels()


if __name__=="__main__":
  main()