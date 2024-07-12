import streamlit as st
import time
import random

st.title("Real-time Data Updates")

# Function to simulate real-time data
def get_data():
    while True:
        yield random.randint(1, 100)
        time.sleep(1)

data_generator = get_data()

# Display real-time data
st.write("Real-time Data:")
latest_data = st.empty()
for value in data_generator:
    latest_data.text(f"Latest Data: {value}")
