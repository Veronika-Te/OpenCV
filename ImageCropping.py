import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def read_image(path):
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 1)
  cv.imshow('Grayscale image', image)
  plt.imshow(cv.cvtColor(image,cv.COLOR_BGR2RGB))
  cv.waitKey(0)
  cv.destroyAllWindows()
  return image

def check_sizes(image: np.ndarray):
  height, width= image.shape[:2]
  aspect_ratio=width/height
  # print(height)
  # print(width)
  # print(f"Aspect Ratio {aspect_ratio}")
  print("____")
  print(image.shape) #(472, 640, 3)
  return width, height

def crop_image(image: np.ndarray,x1,y1,x2,y2):
  """Cropping an image"""
  cropped_image = image[135:280, 150:330]
  cv.imshow("cropped", cropped_image)
  #cv.imwrite("Cropped Image.jpg", cropped_image)
  cv.waitKey(0)
  cv.destroyAllWindows()


 
def main():
  path='media/geometric.jpg'
  image=read_image(path)
  check_sizes(image)
  row_x=135
  row_y=280

  col_x=150
  col_y=330
  crop_image(image, row_x,row_y,col_x,col_y )

  

if __name__=="__main__":
  main()