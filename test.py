from traceback import print_tb
from turtle import screensize
import cv2

import mediapipe as mp
import pyautogui


face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x  * frame_w)
            y = int(landmark.y  * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x * 1.2
                screen_y = screen_h / frame_h * y * 1.2
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x  * frame_w)
            y = int(landmark.y  * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y - left[1].y) < 0.007:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('eye controlled mouse', frame)
    cv2.waitKey(1)
        
        
        #print(landmarks)