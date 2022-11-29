from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정
def jamoComb7():
    path = './testImg/jamo/background6O'
    if not os.path.exists(path):
        os.makedirs(path)

    for j in [29,30,31,34,35,36,39]:
        src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
        for i in range (1,20):   #자음
            src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
            src2 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(i)+'.png') #초성
            src3 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(j)+'.png') #중성

            rows, cols, channels = src3.shape #로고파  일 픽셀값 저장
            
            #gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                #모음 먼저, 자음을 그 위에
            src1[90:rows+90, 50:cols+50] = src3
            cv2.imshow('jaem', src3)
            width, height = src2.shape[:2]
            src1[65:width+65, 40:40+height] = src2
            cv2.imshow('moem', src1)

            if(0 < i < 10): stri="0"+str(i)
            else: stri=str(i)
            if(0 < j-19 < 10): strj="0"+str(j-19)
            else: strj=str(j-19)
            cv2.imwrite(path+'/letter'+stri+'_'+strj+'.png', src1)
            
            #cv2.imwrite('./testImg/jamo/backgroundO/letter'+str(i)+'_'+str(j)+'.png', src1)

    cv2.waitKeyEx()
    cv2.destroyAllWindows()
jamoComb7()