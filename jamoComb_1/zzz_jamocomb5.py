from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

def jamoComb5():
    #directory 존재하지 않은 경우 생성
    path = './testImg/jamo/background6O'
    #path = './cropImg'
    if not os.path.exists(path):
        os.makedirs(path)

    #for k in range(1,20):
    for k in [1,2,3,4,6,7,8,10,11,12,13,15,16,17,18,19]:  
        for j in [28,32,33,37,38]:
            for i in range (1, 20):
                src1 = cv2.imread('./testImg/bg180x210.png')
                src2 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(i)+'.png') 
                src3 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(j)+'.png')
                src4 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(k)+'.png')

                rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
                roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
                #cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))

                #gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                #ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
                #mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

                src1[30:rows+30, 60:cols+60] = src2
                cv2.imshow('jaem', src1)
                width, height = src3.shape[:2]
                src1[90:width+90, 55:55+height] = src3
                cv2.imshow('moem', src1)
                width, height = src4.shape[:2]
                src1[125:width+125, 60:60+height] = src4
                cv2.imshow('jong', src1)

                if(0 < i < 10): stri="0"+str(i)
                else: stri=str(i)
                if(0 < j-19 < 10): strj="0"+str(j-19)
                else: strj=str(j-19)
                if(0 < k < 10): strk="0"+str(k)
                else: strk=str(k)
                #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'.png', src1)
                cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'.png', src1)

    cv2.waitKeyEx()
    cv2.destroyAllWindows()

jamoComb5()