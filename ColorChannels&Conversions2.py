import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def split_merge_color_channels(path:str):
  """Splitting and merging color channels"""
  if not path or not os.path.exists(path):
    return
  
  img_bgr=cv2.imread('media/lake.jpg', cv2.IMREAD_COLOR)
  b,g,r=cv2.split(img_bgr)

  #show channels
  plt.figure(figsize=[20,5])
  plt.subplot(141),plt.imshow(r, cmap='gray'); plt.title("Red Channel");
  plt.subplot(142),plt.imshow(g, cmap='gray'); plt.title("Green Channel");
  plt.subplot(143),plt.imshow(b, cmap='gray'); plt.title("Blue Channel"); 

  imMerged= cv2.merge((b,g,r))
  plt.subplot(144); plt.imshow(imMerged[:,:,::-1]); plt.title("Merged Output")
  plt.show()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def change_to_hsv(path:str):
  """Changing color space to HSV"""
  if not path or not os.path.exists(path):
    return
  img_hsv=cv2.imread('media/lake.jpg', cv2.COLOR_BGR2HSV)
  h,s,v=cv2.split(img_hsv)
  plt.figure(figsize=[20,5])
  plt.subplot(141),plt.imshow(img_hsv, cmap='gray'); plt.title("Original"); 
  plt.subplot(142),plt.imshow(h, cmap='gray'); plt.title("H Channel");
  plt.subplot(143),plt.imshow(s, cmap='gray'); plt.title("S Channel");
  plt.subplot(144),plt.imshow(v, cmap='gray'); plt.title("V Channel");
  
  plt.show()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def raise_H_channel_hsv(path:str, h_channel: int):
  """Modifying H channel, by rising it """
  if not path or not os.path.exists(path):
    return
  if not h_channel or not isinstance(h_channel, int):
    return
  img_hsv=cv2.imread('media/lake.jpg', cv2.COLOR_BGR2HSV)
  h,s,v=cv2.split(img_hsv)
  h_new=h+h_channel
  img_merged=cv2.merge((h_new,s,v))
  img_rgb=cv2.cvtColor(img_merged,cv2.COLOR_HSV2RGB)
  plt.figure(figsize=[20,5])

  plt.subplot(141),plt.imshow(img_rgb, cmap='gray'); plt.title("Modified"); 
  plt.subplot(142),plt.imshow(h, cmap='gray'); plt.title("H Channel");
  plt.subplot(143),plt.imshow(s, cmap='gray'); plt.title("S Channel");
  plt.subplot(144),plt.imshow(v, cmap='gray'); plt.title("V Channel");
  
  plt.show()
  cv2.waitKey(0)
  cv2.destroyAllWindows()
 

def main():
  input_path='media/lake.jpg'
  #split_merge_color_channels(input_path)
  #change_to_hsv(input_path)
  h_channel=10
  raise_H_channel_hsv(input_path, h_channel)

if __name__=="__main__":
  main()
  