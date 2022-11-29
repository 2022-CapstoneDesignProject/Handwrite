from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

#배경 없애기 전에 먼저 자음 모음 합쳐보기
#여기서 위치 및 크기 조정

# for문의 range 값 조절하여 파일 여러개 생성


#받침자음 두개 가능한 경우 ㄳ  ㄵㄶ  ㄺㄻㄼㄽㄾㄿㅀ  ㅄ
def jamoComb6():

    #directory 존재하지 않은 경우 생성
    path = './testImg/jamo/background6O'
    if not os.path.exists(path):
        os.makedirs(path)
    
    
    
    for k in range(1,20):
        src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
        for j in [28,32,33,37,38]:
            for i in range (1,20):
                src1 = cv2.imread('./testImg/bg180x210.png') #배경파일 읽기
                src2 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(i)+'.png') #초성
                src3 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(j)+'.png') #중성
                src4 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(k)+'.png') #첫번째종성
                    
                rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
                roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.

                gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                #ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
                #mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

                src1[20:rows+20, 60:cols+60] = src2
                #cv2.imshow('jaem', src1)
                width, height = src3.shape[:2]
                src1[80:width+80,55:55+height] = src3
                #cv2.imshow('moem', src1)
                width, height = src4.shape[:2]
                src1[115:width+115, 35:35+height] = src4
                cv2.imshow('jong1', src1)
                if(0 < i < 10): stri="0"+str(i)
                else: stri=str(i)
                if(0 < j-19 < 10): strj="0"+str(j-19)
                else: strj=str(j-19)
                if(0 < k < 10): strk="0"+str(k)
                else: strk=str(k)
                if k == 1: #첫번째 종성이 ㄱ, ㅂ일때 -> 가능한 경우는 ㄳ, ㅄ
                    if(0 < k+1 < 10): strk="0"+str(k+1)
                    else: strk=str(k+1)
                    src5 = cv2.imread('./cropImg/2/cropped/resized/letter10.png') #두번째종성 ㅅ
                    width, height = src5.shape[:2]
                    src1[115:width+115, 90:90+height] = src5
                    #cv2.imshow('jong2', src1)
                    cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_1.png', src1)
                elif k == 8: #첫번째 종성이 ㄱ, ㅂ일때 -> 가능한 경우는 ㄳ, ㅄ
                    if(0 < k+1 < 10): strk="0"+str(k+1)
                    else: strk=str(k+1)
                    src5 = cv2.imread('./cropImg/2/cropped/resized/letter10.png') #두번째종성 ㅅ
                    width, height = src5.shape[:2]
                    src1[115:width+115, 90:90+height] = src5
                    #cv2.imshow('jong2', src1)
                    cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_1.png', src1)
                elif k == 3: #첫번째 종성이 ㄴ일때 -> 가능한 경우는 ㄵ, ㄶ
                    for l in [13,19]:#두번째 종성 ㅈ,ㅎ
                        src5 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(l)+'.png') #두번째종성
                        width, height = src5.shape[:2]
                        src1[115:width+115, 90:90+height] = src5
                        #cv2.imshow('jong2', src1)
                        if l == 13: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_1.png', src1)
                        elif l == 19: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_2.png', src1)
                elif k == 6: #첫번째 종성이 ㄹ일때 -> ㄺㄻㄼㄽㄾㄿㅀ
                    for l in [1,7,8,10,17,18,19]:
                        #t=1
                        src5 = cv2.imread('./cropImg/2/cropped/resized/letter'+str(l)+'.png') #두번째종성
                        width, height = src5.shape[:2]
                        src1[115:width+115, 90:90+height] = src5
                        cv2.imshow('jong2', src1)
                        if l==1: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_1.png', src1)
                        elif l==7: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_2.png', src1)
                        elif l==8: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_3.png', src1)
                        elif l==10: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_4.png', src1)
                        elif l==17: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_5.png', src1)
                        elif l==18: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_6.png', src1)
                        elif l==19: cv2.imwrite(path+'/letter'+stri+'_'+strj+'_'+strk+'_7.png', src1)
                        #t = t+1

                #cv2.imwrite('./testImg/jamo/backgroundO/letter'+str(i)+'_'+str(j)+'_'+str(k)+'.png', src1)

    cv2.waitKeyEx()
    cv2.destroyAllWindows()
jamoComb6()