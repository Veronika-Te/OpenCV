import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import os

def read_grayscale_image(path:str):
  """Reads an image and transforms it into grayscale"""
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 0)
  return image

def binary_threshold(image:np.ndarray,threshold_value = 10):
  """Binary thresholding"""
  th, dst = cv.threshold(image, 0, 255, cv.THRESH_BINARY)
  # Apply basic thresholding
  
  _, thresh_image = cv.threshold(image, threshold_value, 255, cv.THRESH_BINARY)
 
  #Inverse-Binary Thresholding
  _, thresh_image_inv = cv.threshold(image, threshold_value, 255, cv.THRESH_BINARY_INV) 

  plt.subplot(121),plt.imshow(thresh_image),plt.title('Basic Thresholding ')
  plt.subplot(122),plt.imshow(thresh_image_inv),plt.title('Inverse-Binary Thresholding')
  plt.show()
  
def truncation_threshold(image:np.ndarray, threshold_value=10):
  """Truncation Thresholding"""
  _, thresh_image_trunc = cv.threshold(image, threshold_value, 255, cv.THRESH_TRUNC)
  plt.imshow(thresh_image_trunc)
  plt.show()
 
def adaptive_threshold(image: np.ndarray):
  """Adaptive Thresholding"""
  if image is None:
    return
  #The mean of the neighborhood area.
  adaptive_thresh_m = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                     cv.THRESH_BINARY, 11, 2)
  
  #The weighted sum of the neighborhood values.
  adaptive_thresh_g = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY, 11, 2)
  
  plt.subplot(121),plt.imshow(adaptive_thresh_m),plt.title('Adaptive Thresholding (MEAN)')
  plt.subplot(122),plt.imshow(adaptive_thresh_g),plt.title('Adaptive Thresholding (GAUSSIAN)')
  plt.show()

def zero_thresholding(image: np.ndarray, threshold_value = 10):
  """Zero Thresholding"""
  if image is None or not isinstance(image, np.ndarray):
    return
  if not is_valid_threshold_value(threshold_value):
    return
 
  #Zero Thresholding
  _, thresh_image_tozero = cv.threshold(image, threshold_value, 255, cv.THRESH_TOZERO)

  #Zero Inverted Thresholding
  _, thresh_image_tozero_inv = cv.threshold(image, threshold_value, 255, cv.THRESH_TOZERO_INV)

  plt.subplot(121),plt.imshow(thresh_image_tozero),plt.title('Zero Thresholding')
  plt.subplot(122),plt.imshow(thresh_image_tozero_inv),plt.title('Zero Inverted Thresholding')
  plt.show()
 

def is_valid_threshold_value(threshold: int)->bool:
  """Checks if threshold is valid"""
  if not isinstance(threshold, int):
    return False
  #Threshold value must be between 0 and 255.
  if threshold < 0 or threshold> 255:
    return False
  return True


def main():
  path='media/lake.jpg'
  image=read_grayscale_image(path)
  threshold=123
  # binary_threshold(image, threshold)
  # truncation_threshold(image, threshold)
  # adaptive_threshold(image)
  zero_thresholding(image, threshold)

if __name__=="__main__":
  main()