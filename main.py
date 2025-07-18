import cv2 , pyautogui, mediapipe as mp

phone_ip = "192.168.0.102:8080"
url = f"http://{phone_ip}/video"

cap = cv2.VideoCapture(url)
hand_detector = mp.solutions.hands.Hands()

drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

while True:
  _, frame = cap.read()
  frame = cv2.flip(frame, 1)
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  frame_width, frame_height, _ = frame.shape
  output = hand_detector.process(rgb_frame)
  hands = output.multi_hand_landmarks
  index_y = 0

  if hands :
    for hand in hands :
      drawing_utils.draw_landmarks(frame, hand)
      landmarks = hand.landmark
      for id, landmark in enumerate(landmarks):
        x = int(landmark.x * frame_width)
        y = int(landmark.y * frame_height)
        if id == 8 :
          cv2.circle(img=frame,center=(x,y), radius=10, color=(0,255,255))
          index_x = screen_width / frame_width * x
          index_y = screen_height / frame_height * y
          pyautogui.moveTo(index_x, index_y)
        if id == 4 :
          cv2.circle(img=frame,center=(x,y), radius=10, color=(0,255,255))
          thumb_x = screen_width / frame_width * x
          thumb_y = screen_height / frame_height * y
          if abs(index_y - thumb_y) < 20 :
            pyautogui.click()
            pyautogui.sleep(1)

  cv2.imshow('Virtual Mouse', frame)
  cv2.waitKey(delay=1)
