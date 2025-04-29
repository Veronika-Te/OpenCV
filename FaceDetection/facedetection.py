import cv2
import os

def detect_and_display(frame, face_cascade, eyes_cascade):
    """Detects face and eyes within the face"""
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Equalizes the histogram, improving contrast.
    frame_gray = cv2.equalizeHist(frame_gray)

    # Face detection
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        cv2.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h, x:x+w]

        # Eye detection within the face
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (ex, ey, ew, eh) in eyes:
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)
            radius = int(round((ew + eh) * 0.25))
            cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)

    #Result   
    cv2.imshow('Capture - Face detection', frame)

def load_cascades(face_cascade_path, eyes_cascade_path):
  """Loading Haar cascades"""
  if not face_cascade_path or not eyes_cascade_path:
    raise ValueError("Cascade paths must not be empty.")
  if not os.path.exists(face_cascade_path):
    raise FileNotFoundError(f"Face cascade path does not exist: {face_cascade_path}")
  if not os.path.exists(eyes_cascade_path):
    raise FileNotFoundError(f"Eyes cascade path does not exist: {eyes_cascade_path}")
  
  face_cascade = cv2.CascadeClassifier(cv2.samples.findFile(face_cascade_path))
  eyes_cascade = cv2.CascadeClassifier(cv2.samples.findFile(eyes_cascade_path))

  # Checking the download
  if face_cascade.empty():
    print("--(!) Error loading face cascade")
    exit(-1)
  if eyes_cascade.empty():
    print("--(!) Error loading eye cascade")
    exit(-1)

  return face_cascade, eyes_cascade

def video_stream(face_cascade, eyes_cascade):
  """Start the video stream from the camera"""
  camera_device = 0
  cap = cv2.VideoCapture(camera_device)
  if not cap.isOpened():
    print("--(!) Error opening video stream")
    exit(-1)

  while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("--(!) Failed to capture frame - exit")
        break

    detect_and_display(frame, face_cascade, eyes_cascade)
    if cv2.waitKey(10) == 27:  # ESC for exit
        break

  cap.release()
  cv2.destroyAllWindows()


def main():
  face_cascade_path="FaceDetection/data/haarcascades/haarcascade_frontalface_alt.xml"
  eyes_cascade_path="FaceDetection/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"

  try:
    res=load_cascades(face_cascade_path, eyes_cascade_path)
    face_cascade=res[0]
    eyes_cascade=res[1]
  except (ValueError, FileNotFoundError, IOError) as e:
      print(f"Error loading cascades: {e}")
      return
  video_stream(face_cascade,eyes_cascade)

if __name__=="__main__":
   main()

