import cv2
import numpy as np

# 웹카메라로부터 입력받기
cap = cv2.VideoCapture(0)
while True:
    #카메라로부터 이미지 읽기
    _, frame = cap.read()
    #이미지를 축속해서 출력하기
    frame = cv2.resize(frame, (500,300))
    #윈도우에 이미지 출력하기
    cv2.imshow('OpenCV Web Camera', frame)
    # ESC 또는 Enter키가 입력되면 반복 종료하기
    k = cv2.waitKey(1) # 1m sec 대기
    if k == 27 or k == 13: break
        
cap.release()
cv2.destroyAllWindows() # 윈도우 제거하기