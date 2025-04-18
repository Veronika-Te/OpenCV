import cv2 as cv
import numpy as np
import os

def read_image(path):
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 0)
  cv.imshow('Grayscale image', image)
  return image

def rotate_image():
  pass
  
def main():
  path='media/geometric.jpg'
  image=read_image(path)


if __name__=="__main__":
  main()