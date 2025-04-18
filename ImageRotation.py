import cv2 as cv
import numpy as np
import os

def read_image(path):
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 1)
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
  
def main():
  path='media/geometric.jpg'
  image=read_image(path)
  angle=90
  rotate_image(image, angle)


if __name__=="__main__":
  main()