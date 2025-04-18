import cv2 as cv
import os

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
    print(f"FPS video: {fps}")
  while True:
    ret, frame =cap.read()
    if not ret:
      print ("Can't receive frame (stream end?). Exiting ...")
      break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # Displaying the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
      break

  cap.release()
  cv.destroyAllWindows()

#TODO CHECK write function
def write_video(input_path:str, output_path:str):
  cap=cv.VideoCapture(input_path)
  if not cap.isOpened():
    print("Error: Could not open video file.")
    #exit()
    return
  
  fps = int(cap.get(cv.CAP_PROP_FPS))
  frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

  fourcc=cv.VideoWriter_fourcc(*'XVID')
  out=cv.VideoWriter(output_path, fourcc,fps,(frame_width, frame_height))
  
  while cap.isOpened():
    ret, frame=cap.read()
    if not ret:
      print("End of video or error occured")
      break
    gray_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(gray_frame)
    cv.imshow("Grayscale Video", gray_frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
      break
    
  print("ok")
  cap.release()
  out.release()
  cv.destroyAllWindows()
  


if __name__=="__main__":
  
  input_file = 'media/traffic.mp4'
  #inpt='output_grayscale.mp4'
  output_file = 'output_grayscale.avi'
  read_video(input_file)
  write_video(input_file,output_file)