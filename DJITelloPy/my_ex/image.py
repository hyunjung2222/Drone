#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 이미지 파일이 존재하는지 확인
img = cv2.imread('/Users/ihyeonjeong/workspace/특강/DJtelloPy/my_ex/images/dog.jpeg')
if img is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인해주세요.")
    exit()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,127,255,0)

#contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
#hierachy는 contours line의 계층 구조
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

