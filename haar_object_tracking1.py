import cv2
import os

# Directory containing the OTB-100 dataset videos
videos_directory = "/home/vishnu1601/Documents/Finalproject/videos"  # Replace with the actual directory

# Path to Haar Cascade classifier XML file
face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
# cascade_path = "/home/vishnu1601/Documents/Finalproject/cascade.xml"  # Replace with the actual path

# List all video files in the directory
video_files = [f for f in os.listdir(videos_directory) if f.endswith('.avi') or f.endswith('.mp4')]

# Loop through each video file
for video_file in video_files:
    video_path = os.path.join(videos_directory, video_file)

    # Read the video file
    video_capture = cv2.VideoCapture(video_path)

    # Loop through the frames and perform object tracking
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Convert frame to grayscale for Haar Cascade detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect objects using the Haar Cascade
        objects = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the frame with detected objects
        cv2.imshow("Object Detection", frame)
        
        # Press 'q' to quit the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()
