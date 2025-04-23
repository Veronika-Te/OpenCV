import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def read_image(path):
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, 1)
  cv.imshow('Image', image)
  plt.imshow(cv.cvtColor(image,cv.COLOR_BGR2RGB))
  cv.waitKey(0)
  cv.destroyAllWindows()
  return image

def drawline(image):
  imageLine = image.copy()
  #Draw the image from point A to B
  pointA = (24,1075)
  pointB = (5957,997)
  cv.line(imageLine, pointA, pointB, (255, 255, 0), thickness=100, lineType=cv.LINE_AA)
  #cv.imshow('Image Line', imageLine)
  plt.imshow(cv.cvtColor(imageLine,cv.COLOR_BGR2RGB))
  cv.waitKey(0)
  cv.destroyAllWindows()

def drawcircle(image):
  imageCircle = image.copy()
  circle_center = (3278,1946)
  radius =300
  #set thickness=100 for hollow circle
  cv.circle(imageCircle, circle_center, radius, (0, 255, 255), thickness=cv.FILLED, lineType=cv.LINE_AA) 
  # Display the result
  #cv.imshow("Image Circle",image)
  plt.imshow(cv.cvtColor(imageCircle,cv.COLOR_BGR2RGB))
  cv.waitKey(0)

def drawrectangle(image):
  imageRectangle = image.copy()
  start_point =(2068, 1045)
  end_point =(4270,3634)
  plt.imshow(cv.cvtColor(imageRectangle,cv.COLOR_BGR2RGB))
  cv.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness=50, lineType=cv.LINE_8) 
  # display the output
  cv.imshow('imageRectangle', imageRectangle)
  cv.waitKey(0)


def main():
  path='media/dog.jpg'
  image=read_image(path)
  #drawline(image)
  #drawcircle(image)
  drawrectangle(image)


if __name__=="__main__":
  main()