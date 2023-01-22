import cv2
from time import sleep

# Open the video file
if not int(input("What do u want ti capture? (1 to real time webcam, 0 to video file video.mp4)")):
    cap = cv2.VideoCapture("video.mp4")
else:
    cap = cv2.VideoCapture(0)

# Define the ASCII characters to use for the conversion
chars = " .,:;i1tfLCG08@"

# Run the video loop
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize the frame to a smaller size (optional)
    frame = cv2.resize(frame, (200, 80))

    # Create an empty list to store the ASCII characters
    ascii_art = []

    # Iterate over each pixel in the image
    for y in range(frame.shape[0]):
        row = ""
        for x in range(frame.shape[1]):
            # Get the pixel value (0-255)
            pixel = frame[y, x]
            # Convert the pixel value to an ASCII character
            char = chars[int(pixel / (256 / len(chars)))]
            row += char
        ascii_art.append(row)

    # Print the ASCII art
    for row in ascii_art:
        print(row)

    # Wait for a short time before displaying the next frame
    sleep(1/60)

# Release the video capture object
cap.release()
