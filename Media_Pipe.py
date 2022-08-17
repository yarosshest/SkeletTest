import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# create capture object
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # read frame from capture object
    _, frame = cap.read()
    try:
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(RGB)
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Output', frame)
    except:
        break

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
