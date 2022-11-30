from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정
def jamoComb7():
    path = './comb'
    if not os.path.exists(path):
        os.makedirs(path)

    for j in [29,30,31,34,35,36,39]:
        for i in range (1,20):   #자음
            src1 = cv2.imread('../src/background.png') #배경파일 읽기
            src2 = cv2.imread('./crop/'+str(i)+'.png') #초성
            src3 = cv2.imread('./crop/'+str(j)+'.png') #중성

            rows, cols, channels = src3.shape #로고파  일 픽셀값 저장
            
            #gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                #모음 먼저, 자음을 그 위에
            src1[100:rows+100, 90:cols+90] = src3
            #cv2.imshow('jaem', src3)
            width, height = src2.shape[:2]
            src1[60:width+60, 60:60+height] = src2
            #cv2.imshow('moem', src1)

            #cv2.imwrite(path+'/letter'+stri+'_'+strj+'.png', src1)
            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4) + ".png", src1)
    print("comb7")
    cv2.waitKeyEx()
    cv2.destroyAllWindows()
#jamoComb7()