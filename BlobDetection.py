import cv2 as cv
import numpy as np
import os

def read_grayscale_image(path):
  """Read an image and transforms it into grayscale"""
  if not path or not os.path.exists(path):
    return
  image=cv.imread(path, cv.IMREAD_GRAYSCALE)
  cv.imshow('Image', image)
  cv.waitKey(0)
  return image


def blob_detection_with_params(image:np.ndarray):
  """Blob detection with parameters"""
  if image is None or not isinstance(image, np.ndarray):
    return
  
  params = cv.SimpleBlobDetector_Params()

  params.filterByArea = True
  params.minArea = 100
  params.filterByCircularity = False
  params.filterByConvexity = False
  params.filterByInertia = False

  detector=cv.SimpleBlobDetector_create(params)
 
  # Detect blobs
  keypoints = detector.detect(image)

  if len(keypoints) == 0:
    print("Blobs not found")
  else:
    print(f"Detected {len(keypoints)} blobs")

  return keypoints

def blob_detection(img: np.ndarray):
  """Simple blob detection"""
  if img is None:
    return
  detector=cv.SimpleBlobDetector_create()
  keypoints=detector.detect(img)
  img_with_keypoints=cv.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  cv.imshow("Keypoints", img_with_keypoints)
  img_name='simple_blob_detect.jpg'
  save_image(img_with_keypoints, img_name)# name of image
  cv.waitKey(0)

def draw_keypoints(keypoints:tuple, image: np.ndarray):
  """Draw keypoints on the provided image and displays it."""
  if image is None or keypoints is None:
    return
  if not isinstance(image, np.ndarray) or not isinstance(keypoints, tuple):
    return
  img_with_keypoints = cv.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), 
                                        cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  cv.imshow('Blob Detection', img_with_keypoints)
  #Save the image 
  img_name='advanced_blob_detection.jpg'
  save_image(img_with_keypoints, img_name)
  cv.waitKey(0)
  cv.destroyAllWindows()
 
def save_image(image:np.ndarray, img_name:str, folder_path='ouput/'):
  """Save the image"""
  if image is None:
    return
  # Ensure the folder exists
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
  cv.imwrite('output.jpg', image)
  #full path 
  save_path = os.path.join(folder_path, img_name)
  # Save the image 
  cv.imwrite(save_path, image)
  print(f'Image saved to {save_path}')

def main():
  path='media/blobs_dog.jpg' 
  img=read_grayscale_image(path)
  
  #Blob detection with params
  keypoints=blob_detection_with_params(img)
  draw_keypoints(keypoints, img)

  #Simple Blob detection
  # path2='media/blob_test.jpg'
  # img2=read_grayscale_image(path2)
  # blob_detection(img2)

 

if __name__=="__main__":
  main()
  