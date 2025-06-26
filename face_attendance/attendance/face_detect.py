# Face detection logic

#opencv-python==4.6.0.66
#numpy==1.23.4
#pillow==9.2.0

#  Q  TO  CLOSE CAMERA

import cv2

# Start webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

# Check if webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop to continuously get frames
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Show the frame in a window
    cv2.imshow("Webcam Feed", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
