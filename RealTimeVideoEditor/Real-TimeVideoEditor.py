import cv2 as cv
import os
import datetime

pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False


def draw_rectangle(event,x,y,flags,param):
  """Mouse callback"""
  global pt1,pt2,topLeft_clicked,botRight_clicked

  # get mouse click
  if event == cv.EVENT_LBUTTONDOWN:

    if topLeft_clicked == True and botRight_clicked == True:
      topLeft_clicked = False
      botRight_clicked = False
      pt1 = (0,0)
      pt2 = (0,0)

    if topLeft_clicked == False:
      pt1 = (x,y)
      topLeft_clicked = True
            
    elif botRight_clicked == False:
      pt2 = (x,y)
      botRight_clicked = True

def detect_and_display(frame, face_cascade, eyes_cascade):
    """Detects face and eyes within the face"""
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Equalizes the histogram, improving contrast.
    frame_gray = cv.equalizeHist(frame_gray)

    # Face detection
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h, x:x+w]

        # Eye detection within the face
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (ex, ey, ew, eh) in eyes:
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)
            radius = int(round((ew + eh) * 0.25))
            cv.circle(frame, eye_center, radius, (255, 0, 0), 4)
  
    return frame

def load_cascades(face_cascade_path, eyes_cascade_path):
  """Loading Haar cascades"""
  if not face_cascade_path or not eyes_cascade_path:
    raise ValueError("Cascade paths must not be empty.")
  if not os.path.exists(face_cascade_path):
    raise FileNotFoundError(f"Face cascade path does not exist: {face_cascade_path}")
  if not os.path.exists(eyes_cascade_path):
    raise FileNotFoundError(f"Eyes cascade path does not exist: {eyes_cascade_path}")
  
  face_cascade = cv.CascadeClassifier(cv.samples.findFile(face_cascade_path))
  eyes_cascade = cv.CascadeClassifier(cv.samples.findFile(eyes_cascade_path))

  # Checking the download
  if face_cascade.empty():
    print("--(!) Error loading face cascade")
    exit(-1)
  if eyes_cascade.empty():
    print("--(!) Error loading eye cascade")
    exit(-1)

  return face_cascade, eyes_cascade


def read_video(face_cascade, eyes_cascade):
  """Captures live video from the webcam and applies effects interactively, press:
  'v' to flip vertically,
  'h' to flip horizontally,
  'r' to rotate,
  'g' to convert to grayscale,
  's' to switch to HSV,
  'l' for LAB,
  'b' to blur,
  'n' for median filtering,
  'd' to draw shapes,
  'q' to exit
  Include face detection and overlay the current time."""
  camera_device = 0
  cap = cv.VideoCapture(camera_device)
  if not cap.isOpened():
    print("--(!) Error opening video stream")
    exit(-1)
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
  

  #flags for transformations
  is_flipped_v = False
  is_flipped_h = False
  is_rotated = False
  #flags for color spaces
  is_grayscale=False
  is_lab = False
  is_hsv=False
  #flags for blurred
  is_gaussian_blurred=False
  is_median_blurred=False
  # #drawing enabled
  drawing_enabled = False

  # Set the mouse callback function for the window
  cv.namedWindow('Video Stream', cv.WINDOW_AUTOSIZE)
  cv.setMouseCallback('Video Stream', draw_rectangle)

  while True:
    ret, frame =cap.read()
    if not ret:
      print ("Can't receive frame (stream end?). Exiting ...")
      break
    
    #Write the date time in the video frame 
    font = cv.FONT_HERSHEY_SIMPLEX
    date_time = str(datetime.datetime.now())
    frame = cv.putText(frame, date_time,(10, 1000),font, 1,(255, 0, 0), 4, cv.LINE_8)
    
    #Face Detection
   # frame=detect_and_display(frame, face_cascade, eyes_cascade)

    #Transformations
    if is_rotated:
      frame=cv.flip(frame, -1)
    if is_flipped_v:
      frame = cv.flip(frame, 0)
    if is_flipped_h:
      frame=cv.flip(frame, 1)

    #ColorSpaces
    if is_grayscale:
      frame=cv.cvtColor(frame, cv.COLOR_BGRA2GRAY)
    if is_lab:
      frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    if is_hsv:
      frame=cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Blurred
    if is_gaussian_blurred:
      frame=cv.GaussianBlur(frame, (15, 15), 0)
    if is_median_blurred:
      frame=cv.medianBlur(frame,ksize=3)


    # Drawing logic
    if drawing_enabled:
      
      if topLeft_clicked:
        if is_grayscale:
                # Use a grayscale color (white) for single-channel images
          cv.circle(frame, center=pt1, radius=5, color=255, thickness=-1)
        else:
          cv.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)
      if topLeft_clicked and botRight_clicked:
        if is_grayscale:
          cv.rectangle(frame, pt1, pt2, color=255, thickness=2)
        else:
          cv.rectangle(frame, pt1, pt2, color=(0, 0, 255), thickness=2)
    
    cv.imshow('Video Stream', frame)
    
    # Displaying the resulting frame
    key = cv.waitKey(1) & 0xFF
  
    
    #Tranformations
    if key == ord('v'): #flip vertically
      is_flipped_v= not is_flipped_v
    if key == ord('h'): #flip horizontally
      is_flipped_h=not is_flipped_h
    if key==ord('r'): #rotate
      is_rotated=not is_rotated

    #Color spaces
    if key == ord('g'): #grayscale
      is_grayscale=not is_grayscale
    if key==ord('s'): #switch to HSV
      is_hsv=not is_hsv
    if key==ord('l'): # switch to LAB,
      is_lab=not is_lab

    #Blurred
    if key == ord('b'): #gaussian filtering
      is_gaussian_blurred=not is_gaussian_blurred
    if key == ord('n'): #median filtering
      is_median_blurred=not is_median_blurred

    if key == ord('q'):
      break

    #Drawing
    if key==ord('d'):
      drawing_enabled = not drawing_enabled

    if topLeft_clicked:
      cv.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
    if topLeft_clicked and botRight_clicked:
      cv.rectangle(frame, pt1, pt2, (0, 0, 255), 2)
       # Display the resulting frame
    cv.imshow('Video Stream', frame)


  cap.release()
  cv.destroyAllWindows()

def main():
  face_cascade_path="RealTimeVideoEditor/data/haarcascades/haarcascade_frontalface_alt.xml"
  eyes_cascade_path="RealTimeVideoEditor/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"

  try:
    res=load_cascades(face_cascade_path, eyes_cascade_path)
    face_cascade=res[0]
    eyes_cascade=res[1]
    
  except (ValueError, FileNotFoundError, IOError) as e:
    print(f"Error loading cascades: {e}")
  #read_video(face_cascade, eyes_cascade)
  read_video(face_cascade,eyes_cascade)

if __name__=="__main__":
  main()

  