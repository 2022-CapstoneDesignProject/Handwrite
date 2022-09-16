# apple.jpg 그림에 opencv_logo 그림을 Mask_inverse하여 합성.
 
import cv2
import numpy as np

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 
src2 = cv2.imread('./testImg/1.png') #ㄱ파일 읽기
src3 = cv2.imread('./testImg/2.png') #ㅏ파일 읽기

rows, cols, channels = src2.shape #로고파일 픽셀값 저장
roi = src1[50:rows+50,50:cols+50] #로고파일 필셀값을 관심영역(ROI)으로 저장함.

gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

src1_bg = cv2.bitwise_and(roi,roi,mask=mask) #배경에서만 연산 = src1 배경 복사

#cv2.imshow('src1_bg',src1_bg)
 
src2_fg = cv2.bitwise_and(src2,src2, mask = mask_inv) #로고에서만 연산
#cv2.imshow('src2_fg',src2_fg)

dst = cv2.bitwise_or(src1_bg, src2_fg) #src1_bg와 src2_fg를 합성

#cv2.imshow('dst',dst)
src1[60:rows+60,0:cols+0] = dst #src1에 dst값 합성

####################################두번째이미지(모음)합성

rows, cols, channels = src3.shape #로고파일 픽셀값 저장
roi = src1[50:rows+50,50:cols+50] #로고파일 필셀값을 관심영역(ROI)으로 저장함.

gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

src1_bg = cv2.bitwise_and(roi,roi,mask=mask) #배경에서만 연산 = src1 배경 복사

cv2.imshow('src1_bg',src1_bg)
 
src3_fg = cv2.bitwise_and(src3,src3, mask = mask_inv) #로고에서만 연산
#cv2.imshow('src2_fg',src3_fg)

dst2 = cv2.bitwise_or(src1_bg, src3_fg) #src1_bg와 src2_fg를 합성

cv2.imshow('dst2',dst2)
src1[50:rows+50, 50:cols+50] = dst2 #src1에 dst값 합성


cv2.imshow('result',src1)
cv2.waitKeyEx()
cv2.destroyAllWindows()
