from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정


# for문의 range 값 조절하여 파일 여러개 생성

def jamoComb4():

    #directory 존재하지 않은 경우 생성
    path = './testImg/jamo/background6O'
    if not os.path.exists(path):
        os.makedirs(path)

    src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기

    for j in [28,32,33,37,38]:
        src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
        for i in range (1,20):
            src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
            src2 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(i)+'.png') 
            src3 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(j)+'.png')

            rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
            roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
            #cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))

            #gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
            #ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
            #mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

            src1[50:rows+50, 60:cols+60] = src2
            cv2.imshow('jaem', src1)
            width, height = src3.shape[:2]
            src1[110:width+110, 55:55+height] = src3
            cv2.imshow('moem', src1)

            if(0 < i < 10): stri="0"+str(i)
            else: stri=str(i)
            if(0 < j-19 < 10): strj="0"+str(j-19)
            else: strj=str(j-19)
        
            cv2.imwrite(path+'/letter'+stri+'_'+strj+'.png', src1)

            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j)+'.png', src1)

    cv2.waitKeyEx()
    cv2.destroyAllWindows()
jamoComb4()