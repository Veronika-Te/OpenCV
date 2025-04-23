import cv2 as cv
import os
import time

def read_video(input_path :str):
  if not os.path.exists(input_path) or not input_path:
    return
  #cap=cv.VideoCapture('0') #video from webcam
  cap=cv.VideoCapture(input_path)
  if not cap.isOpened():
    print("Cannot open video")
    exit()
  else:
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    duration = frame_count / fps

    print(f"FPS video: {fps}")
    print(f"Total frames: {frame_count}")
    print(f"Resolution: {int(width)}x{int(height)}")
    print(f"Duration: {duration:.2f} seconds")

  while True:
    ret, frame =cap.read()
    if not ret:
      print ("Can't receive frame (stream end?). Exiting ...")
      break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Displaying the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv.destroyAllWindows()

def write_video(input_path:str, output_path:str):
  cap=cv.VideoCapture(input_path)
  if not cap.isOpened():
    print("Error: Could not open video file.")
    #exit()
    return
  
  fps = int(cap.get(cv.CAP_PROP_FPS))
  frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

  # fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D') 
  # fourcc=cv.VideoWriter_fourcc(*'XVID')
  #fourcc=cv.VideoWriter_fourcc(*'XVID')
  fourcc = cv.VideoWriter_fourcc(*'avc1') 
  out_gray = cv.VideoWriter(output_path, fourcc, int(fps),(int(frame_width), int(frame_height)), isColor=False)
  while cap.isOpened():
    ret, frame=cap.read()
    if ret is True:
      gray_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
      out_gray.write(gray_frame)
      cv.imshow("Grayscale Video", gray_frame)
      if cv.waitKey(1) & 0xFF==ord('q'):
        break
    else:
      break
    
  print("Video processing completed")
  cap.release()
  out_gray.release()
  cv.destroyAllWindows()
  


if __name__=="__main__":
  
  input_file = 'media/traffic.mp4'
  #inpt='output_grayscale.mp4'
  output_file = 'output_grayscale.avi'
  read_video(input_file)

  #write_video(input_file,output_file)
import cv2 as cv
import os
import time

def read_video(input_path :str):
  if not os.path.exists(input_path) or not input_path:
    return
  #cap=cv.VideoCapture('0') #video from webcam
  cap=cv.VideoCapture(input_path)
  if not cap.isOpened():
    print("Cannot open video")
    exit()
  else:
    fps = cap.get(cv.CAP_PROP_FPS)
    frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    duration = frame_count / fps

    print(f"FPS video: {fps}")
    print(f"Total frames: {frame_count}")
    print(f"Resolution: {int(width)}x{int(height)}")
    print(f"Duration: {duration:.2f} seconds")

  while True:
    ret, frame =cap.read()
    if not ret:
      print ("Can't receive frame (stream end?). Exiting ...")
      break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Displaying the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv.destroyAllWindows()

def write_video(input_path:str, output_path:str):
  cap=cv.VideoCapture(input_path)
  if not cap.isOpened():
    print("Error: Could not open video file.")
    #exit()
    return
  
  fps = int(cap.get(cv.CAP_PROP_FPS))
  frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

  # fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D') 
  # fourcc=cv.VideoWriter_fourcc(*'XVID')
  #fourcc=cv.VideoWriter_fourcc(*'XVID')
  fourcc = cv.VideoWriter_fourcc(*'avc1') 
  out_gray = cv.VideoWriter(output_path, fourcc, int(fps),(int(frame_width), int(frame_height)), isColor=False)
  while cap.isOpened():
    ret, frame=cap.read()
    if ret is True:
      gray_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
      out_gray.write(gray_frame)
      cv.imshow("Grayscale Video", gray_frame)
      if cv.waitKey(1) & 0xFF==ord('q'):
        break
    else:
      break
    
  print("Video processing completed")
  cap.release()
  out_gray.release()
  cv.destroyAllWindows()
  


if __name__=="__main__":
  
  input_file = 'media/traffic.mp4'
  #inpt='output_grayscale.mp4'
  output_file = 'output_grayscale.avi'
  #read_video(input_file)

  write_video(input_file,output_file)