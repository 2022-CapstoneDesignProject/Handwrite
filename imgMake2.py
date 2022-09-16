import sys, cv2
from matplotlib import pyplot as plt
import numpy as np

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 
src2 = cv2.imread('./testImg/1.png') #ㄱ파일 읽기
src3 = cv2.imread('./testImg/2.png') #ㅏ파일 읽기
#src2Gray = cv2.imread('./testImg/1.png', cv2.IMREAD_GRAYSCALE)
src2Gray = cv2.cvtColor(src2, cv2.COLOR_RGB2GRAY)
#ret, src2mask = cv2.threshold(src2Gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경


blur = cv2.GaussianBlur(src2Gray, ksize=(5, 5), sigmaX=0)
ret, src2mask = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY)
src2Binary = cv2.bitwise_not(src2mask)

edged = cv2.Canny(blur, 10, 250)


cv2.imshow('img1', src2)
cv2.imshow('edged', edged)

cv2.waitKeyEx()
cv2.destroyAllWindows()