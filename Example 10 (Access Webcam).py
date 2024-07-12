import cv2
import streamlit as st
import time

cam = cv2.VideoCapture(0)

st.title("Video Capture")

framePlaceholder = st.empty()


cTime = 0
pTime = 0

stopButton = st.button("Stop")
while True:

    Success, frame = cam.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    framePlaceholder.image(frame, channels="RGB")
    
    key = cv2.waitKey(1)

    if key == ord('q') or stopButton:
        cam.release()
        cv2.destroyAllWindows()
        break


cam.release()
cv2.destroyAllWindows()