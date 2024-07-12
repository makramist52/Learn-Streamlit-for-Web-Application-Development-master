import cv2
import mediapipe as mp
import streamlit as st
import tempfile
import time
import PoseModule as pm

cam = cv2.VideoCapture(0)

st.title("Video Capture")

framePlaceholder = st.empty()


cTime = 0
pTime = 0
detector = pm.poseDetector()

stopButton = st.button("Stop")
while True:

    Success, frame = cam.read()
    frame = detector.findPose(frame)
    lm = detector.findPosLm(frame)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

    # cv2.imshow("Pose Estimation", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    framePlaceholder.image(frame, channels="RGB")
    
    key = cv2.waitKey(1)

    if key == ord('q') or stopButton:
        cam.release()
        cv2.destroyAllWindows()
        break


cam.release()
cv2.destroyAllWindows()