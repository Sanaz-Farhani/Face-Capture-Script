# Face-Capture-Script
This project is a simple Python script that captures live video from the user's webcam, detects faces in real-time, and saves a cropped image of the detected face when requested.

📸 Face Capture Script (Python + OpenCV)

This project is a simple Python script that captures live video from the user's webcam, detects faces in real-time, and saves a cropped image of the detected face when requested.

🚀 Features

Live webcam video stream using OpenCV

Real-time face detection with Haar Cascade classifier

Automatic cropping of detected faces

Save the captured face image by pressing s

Exit the program anytime with q

Saves the file using the user’s input as the image name

🛠️ How It Works

The script connects to your webcam and starts streaming video.

It converts each frame to grayscale for faster face detection.

Haar Cascade (haarcascade_frontalface_default.xml) is used to locate faces.

A rectangle is drawn around detected faces in the live feed.

Press:

s → Save the cropped face image

q → Quit the program

📂 Output

The captured face image is saved to the following path:

D:/face/<name_input>.jpg

📦 Requirements

Python 3.x

OpenCV (pip install opencv-python)
