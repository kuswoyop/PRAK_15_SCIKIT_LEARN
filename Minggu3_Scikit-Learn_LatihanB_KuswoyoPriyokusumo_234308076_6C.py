import cv2
import mediapipe as mp
import numpy as np

mp.pose = mp.solutions.pose
pose = mp.pose.Pose()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)
    text = "Tidak terdetaksi"
    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp.pose.POSE_CONNECTIONS)
        landmarks = results.pose_landmarks.landmark

        hip = landmarks[mp.pose.PoseLandmark.LEFT_HIP.value]
        knee = landmarks[mp.pose.PoseLandmark.LEFT_KNEE.value]
        ankle = landmarks[mp.pose.PoseLandmark.LEFT_ANKLE.value]

        if knee.y > hip.y:
            text = "Berdiri"
        else:
            text = "Duduk"

    cv2.putText(frame, text, (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
    cv2.imshow("Deteksi Pose", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()