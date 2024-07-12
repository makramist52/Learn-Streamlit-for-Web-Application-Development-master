import streamlit as st
import cv2
import numpy as np

st.title("Real-time Object Detection with Webcam")

# Create a video capture object for the webcam
video_capture = cv2.VideoCapture(0)

framePlaceholder = st.empty()

# Initialize trackbar values
hue_low = 0
hue_high = 179
saturation_low = 0
saturation_high = 255
value_low = 0
value_high = 255

# Create a sidebar for trackbar controls
st.sidebar.header("HSV Range Selection")
hue_low = st.sidebar.slider("Hue Low", 0, 179, 0)
hue_high = st.sidebar.slider("Hue High", 0, 179, 179)
saturation_low = st.sidebar.slider("Saturation Low", 0, 255, 0)
saturation_high = st.sidebar.slider("Saturation High", 0, 255, 255)
value_low = st.sidebar.slider("Value Low", 0, 255, 0)
value_high = st.sidebar.slider("Value High", 0, 255, 255)

while True:
    # Read a frame from the webcam
    ret, frame = video_capture.read()
    
    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask using the selected HSV range
    lower_range = np.array([hue_low, saturation_low, value_low])
    upper_range = np.array([hue_high, saturation_high, value_high])
    mask = cv2.inRange(hsv_frame, lower_range, upper_range)
    
    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Display the original frame and the detected object
    # st.image([frame, result], caption=["Original Frame", "Detected Object"], channels="BGR")
    # frame = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    framePlaceholder.image(result, channels="RGB")
