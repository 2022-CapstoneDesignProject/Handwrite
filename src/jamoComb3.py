from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

# for문의 range 값 조절하여 파일 여러개 생성

#받침자음 두개 가능한 경우 ㄳ  ㄵㄶ  ㄺㄻㄼㄽㄾㄿㅀ  ㅄ
def jamoComb3():

    #directory 존재하지 않은 경우 생성
    path = './comb'
    if not os.path.exists(path):
        os.makedirs(path)
    
    for k in range(1,20):
        for j in [20,21,22,23,24,25,26,27,40]:
            for i in range (1,20):
                #src1 = cv2.imread('../src/background.png') #배경파일 읽기
                src1 = cv2.imread('../src/180.png')
                src2 = cv2.imread('./crop/'+str(i)+'.png') #초성
                src3 = cv2.imread('./crop/'+str(j)+'.png') #중성
                src4 = cv2.imread('./crop/'+str(k)+'.png') #첫번째종성
                    
                rows, cols, channels = src2.shape #로고파  일 픽셀값 저장
                roi = src1[50:rows+50,50:cols+50] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
                #cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))

                gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
                ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경

                #초성 세팅
                src1[30:rows+30, 30:cols+30] = src2
                #중성 세팅
                width, height = src3.shape[:2]
                src1[25:width+25, 90:90+height] = src3
                #종성 세팅
                width, height = src4.shape[:2]
                src1[80:width+80, 30:30+height] = src4

                if k == 1: #첫번째 종성이 ㄱ, ㅂ일때 -> 가능한 경우는 ㄳ, ㅄ
                    src5 = cv2.imread('./crop/10.png') #두번째종성 ㅅ
                    width, height = src5.shape[:2]
                    src1[80:width+80, 90:90+height] = src5
                    cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k+1).zfill(3)+"_" +str(1).zfill(3) + ".png", src1)
                elif k == 8: #첫번째 종성이 ㄱ, ㅂ일때 -> 가능한 경우는 ㄳ, ㅄ
                    src5 = cv2.imread('./crop/10.png') #두번째종성 ㅅ
                    width, height = src5.shape[:2]
                    src1[80:width+80, 90:90+height] = src5
                    cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4) +"_"+str(k).zfill(3)+"_"+str(1).zfill(3)+ ".png", src1)
                elif k == 3: #첫번째 종성이 ㄴ일때 -> 가능한 경우는 ㄵ, ㄶ
                    for l in [13,19]:#두번째 종성 ㅈ,ㅎ
                        src5 = cv2.imread('./crop/'+str(l)+'.png') #두번째종성
                        width, height = src5.shape[:2]
                        src1[80:width+80, 90:90+height] = src5
                        if l == 13: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(1).zfill(3) + ".png", src1)
                        elif l == 19: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_" +str(2).zfill(3) + ".png", src1)
                elif k == 6: #첫번째 종성이 ㄹ일때 -> ㄺㄻㄼㄽㄾㄿㅀ
                    for l in [1,7,8,10,17,18,19]:
                        
                        src5 = cv2.imread('./crop/'+str(l)+'.png') #두번째종성
                        width, height = src5.shape[:2]
                        src1[80:width+80, 90:90+height] = src5
                        #cv2.imshow('jong2', src1)
                        if l==1:                  
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(1).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_1.png', src1)
                        elif l==7: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(2).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_2.png', src1)
                        elif l==8: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(3).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_3.png', src1)
                        elif l==10: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(4).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_4.png', src1)
                        elif l==17: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(5).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_5.png', src1)
                        elif l==18: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(6).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_6.png', src1)
                        elif l==19: 
                            cv2.imwrite(path+'/letter'+str(i).zfill(3)+"_"+ str(j-19).zfill(4)+"_"+str(k).zfill(3)+"_"+str(7).zfill(3) + ".png", src1)
                            #cv2.imwrite(path+'/letter'+str(i)+'_'+str(j-19)+'_'+str(k)+'_7.png', src1)

                
    print("comb3")
    cv2.waitKeyEx()
    cv2.destroyAllWindows()

#jamoComb3()