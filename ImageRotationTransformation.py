import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import os

def read_image(path):
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, -1)
  cv.imshow('Image', image)
  return image

def check_sizes(image):
  height, width= image.shape[:2]
  aspect_ratio=width/height
  print(f"Aspect Ratio {aspect_ratio}")
  return width, height

def rotate_image(image: np.ndarray, inp_angle:int):
  width, height=check_sizes(image)
  center = (width/2, height/2)
  rotate_matrix = cv.getRotationMatrix2D(center=center, angle=inp_angle, scale=1)
  rotated_image = cv.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
  cv.imshow('Original image', image)
  cv.imshow('Rotated image', rotated_image)
  cv.waitKey(0)
  cv.imwrite('rotated_image.jpg', rotated_image)

def affine_transform(image: np.ndarray):
  rows,cols,ch = image.shape
  pts1 = np.float32([[50,50],[200,50],[50,200]])
  pts2 = np.float32([[10,100],[200,50],[100,250]])
  M = cv.getAffineTransform(pts1,pts2)
  dst = cv.warpAffine(image,M,(cols,rows))
  plt.subplot(121),plt.imshow(image),plt.title('Input')
  plt.subplot(122),plt.imshow(dst),plt.title('Output')
  plt.show()
  
def main():
  path='media/geometric.jpg'
  image=read_image(path)
  angle=90
  rotate_image(image, angle)
  affine_transform(image)


if __name__=="__main__":
  main()