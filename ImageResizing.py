import cv2 as cv
import numpy as np

def read_image(path):
  if not path:
    return
  image=cv.imread(path, 0)
  cv.imshow('Grayscale image', image)
  return image

def check_sizes(image):
  height, width= image.shape[:2]
  aspect_ratio=width/height
  print(f"Aspect Ratio {aspect_ratio}")
  return width, height

def downscale_image(image:np.ndarray , down_width: int, down_height: int):
  if not down_width or not down_height:
    return
  if not isinstance(down_width, int) or not isinstance(down_height, int):
    return
  if not isinstance(image, np.ndarray):
    return
  res=check_sizes(image)
  original_width, original_height=res

  if not down_width<=original_width or not down_height<=original_height:
    return
  down_points=(down_width,down_height)
  resized_down=cv.resize(image, down_points, interpolation=cv.INTER_LINEAR)
  cv.imshow('Resized Down by defining height and width', resized_down)
  cv.waitKey(0)
  cv.destroyAllWindows()

def upscale_image(image: np.ndarray,  up_width: int, up_height: int):
  if not up_width or not up_height:
    return
  if not isinstance(up_width, int) or not isinstance(up_height, int):
    return
  if not isinstance(image, np.ndarray):
    return
  res=check_sizes(image)
  original_width, original_height=res

  if not up_width>=original_width or not up_height>=original_height:
    return
  up_points=(up_width, up_height)
  resized_up=cv.resize(image, up_points, interpolation=cv.INTER_LINEAR)
  cv.imshow('Resized Up by defining height and width', resized_up)
  cv.waitKey(0)
  cv.destroyAllWindows()

def resize_with_scalingfactor(image: np.ndarray):
  #Scaling Up the image 1.2 times by specifying both scaling factors
  scale_up_x = 1.2
  scale_up_y = 1.2
  # Scaling Down the image 0.6 times specifying a single scale factor.
  scale_down = 0.6

  scaled_f_down = cv.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv.INTER_LINEAR)
  scaled_f_up = cv.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv.INTER_LINEAR)
  cv.imshow('Resized Down by defining height and width', scaled_f_down)
  cv.waitKey(0)
  cv.imshow('Resized Up by defining height and width', scaled_f_up)
  cv.waitKey(0)
  cv.destroyAllWindows()
  
def main():
  path='media/geometric.jpg'
  image=read_image(path)

  down_width =300
  down_height=200
  #downscale_image(image,down_width, down_height)

  up_width=1920
  up_height=1000
  #upscale_image(image,up_width,up_height)

  resize_with_scalingfactor(image)

if __name__=="__main__":
  main()