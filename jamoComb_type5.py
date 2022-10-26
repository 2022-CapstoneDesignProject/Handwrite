from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정

# for문의 range 값 조절하여 파일 여러개 생성

def jamoComb5():

    #directory 존재하지 않은 경우 생성
    path = './testImg/jamo/backgroundO'
    if not os.path.exists(path):
        os.makedirs(path)
    
    src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기

    for k in range(1,23):
        for j in range(10,15):         
            for i in range (1,23):
                src2 = cv2.imread('./testImg/jamo/ja'+str(i)+'.png') 
                src3 = cv2.imread('./testImg/jamo/mo'+str(j)+'.png')
                src4 = cv2.imread('./testImg/jamo/ja'+str(k)+'.png')

                rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
                roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
                cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))

                gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
                #mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

                src1[50:rows+50, 100:cols+100] = src2
                cv2.imshow('cho', src1)
                width, height = src3.shape[:2]
                src1[115:width+115, 85:85+height] = src3
                cv2.imshow('jung', src1)
                width, height = src4.shape[:2]
                src1[170:width+170, 100:100+height] = src4
                cv2.imshow('jong', src1)

                cv2.imwrite(path+'/letter'+str(i)+'_'+str(j)+'_'+str(k)+'.png', src1)

    cv2.waitKeyEx()
    cv2.destroyAllWindows()