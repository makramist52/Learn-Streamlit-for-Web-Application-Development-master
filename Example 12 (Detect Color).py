import streamlit as st
import cv2
import numpy as np
import PIL 
from io import BytesIO

st.title("Colored Object Detection with OpenCV")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Initialize default trackbar values
hue_low = 0
hue_high = 179
saturation_low = 0
saturation_high = 255
value_low = 0
value_high = 255

if uploaded_image is not None:
    # Read the uploaded image from its content
    image = PIL.Image.open(uploaded_image)
    image = np.array(image)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create trackbars for HSV range selection
    st.sidebar.header("HSV Range Selection")
    hue_low = st.sidebar.slider("Hue Low", 0, 179, 0)
    hue_high = st.sidebar.slider("Hue High", 0, 179, 179)
    saturation_low = st.sidebar.slider("Saturation Low", 0, 255, 0)
    saturation_high = st.sidebar.slider("Saturation High", 0, 255, 255)
    value_low = st.sidebar.slider("Value Low", 0, 255, 0)
    value_high = st.sidebar.slider("Value High", 0, 255, 255)
    
    # Create a mask using the selected HSV range
    lower_range = np.array([hue_low, saturation_low, value_low])
    upper_range = np.array([hue_high, saturation_high, value_high])
    mask = cv2.inRange(hsv_image, lower_range, upper_range)
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Display the original image and the detected object
    st.image([image, result], caption=["Original Image", "Detected Object"])
