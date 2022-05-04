import cv2
import mediapipe as mp

# set webcam as capture device
cap = cv2.VideoCapture(0)

# set up mediapipe methods for detectors
mpHolistic = mp.solutions.holistic
holistic = mpHolistic.Holistic()
mpDraw = mp.solutions.drawing_utils
drawing_specs = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:                         # initialization condition can be set to: weight sensors changing
    success, img = cap.read()
    if not success:
        break
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = holistic.process(imgRBG)

    mpDraw.draw_landmarks(img, results.face_landmarks, mpHolistic.FACEMESH_CONTOURS, drawing_specs, drawing_specs)
    mpDraw.draw_landmarks(img, results.left_hand_landmarks, mpHolistic.HAND_CONNECTIONS, drawing_specs, drawing_specs)
    mpDraw.draw_landmarks(img, results.right_hand_landmarks, mpHolistic.HAND_CONNECTIONS, drawing_specs, drawing_specs)
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpHolistic.POSE_CONNECTIONS, drawing_specs, drawing_specs)

    # display video capture
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
