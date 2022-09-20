import cv2
import numpy as np

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 
src2 = cv2.imread('./testImg/No1.jpg') #ㄱ파일 읽기
src3 = cv2.imread('./testImg/No2.jpg') #ㅏ파일 읽기

rows, cols, channels = src2.shape #로고파일 픽셀값 저장
#roi = src1[20:rows+20,20:cols+20] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
#cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))
print(rows)
print(cols)
print(channels)

r, c, ch = src1.shape
print(r)
print(c)
print(ch)

#gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
ret, mask = cv2.threshold(src2, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
#mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

roi = src1[0:rows, 0:cols]

#dst2 = cv2.bitwise_or(src2_fg, src3_fg)
#cv2.imshow('dst2', dst2)
 
#src1[30:rows+30,30:cols+30] = src2 #src1에 src2값 합성
#img1 = src1.copy()

dst = cv2.addWeighted(roi, 1, mask, 0.5, 0)

#dst = cv2.bitwise_and(mask, src1)
src1[0:rows, 0:cols] = dst
#img1[30:rows + 30+30, 30:cols +60] = src3
 
cv2.imshow('result',src1)


cv2.waitKeyEx()
cv2.destroyAllWindows()
