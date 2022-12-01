from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정

# for문의 range 값 조절하여 파일 여러개 생성
def jamoComb2():
    #directory 존재하지 않은 경우 생성
    path = './comb'
    if not os.path.exists(path):
        os.makedirs(path)

    #초성, 중성, 자음 1개로 구성된 종성 글자 생성하기
    for k in [1,2,3,4,6,7,8,10,11,12,13,15,16,17,18,19]:
        for j in [20,21,22,23,24,25,26,27,40]:
            for i in range (1, 20):
                #src1 = cv2.imread('../src/background.png')
                src1 = cv2.imread('../src/180.png')
                src2 = cv2.imread('./crop/'+str(i)+'.png') 
                src3 = cv2.imread('./crop/'+str(j)+'.png')
                src4 = cv2.imread('./crop/'+str(k)+'.png')

                rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
                roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
                #cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))

                gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
                #mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

                src1[30:rows+30, 30:cols+30] = src2
                width, height = src3.shape[:2]
                src1[25:width+25, 90:90+height] = src3
                width, height = src4.shape[:2]
                src1[80:width+80, 60:60+height] = src4

                cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3) + ".png", src1)
    print("comb2")
    cv2.waitKeyEx()
    cv2.destroyAllWindows()

#jamoComb2()