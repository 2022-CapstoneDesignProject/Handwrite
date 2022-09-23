from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 
src2 = cv2.imread('./testImg/No1.jpg') #ㄱ파일 읽기
src3 = cv2.imread('./testImg/No2.jpg') #ㅏ파일 읽기
#img = cv2.imread('./testImg/noBg1.jpg')

rows, cols, channels = src2.shape #로고파일 픽셀값 저장
#roi = src1[20:rows+20,20:cols+20] #로고파일 픽셀값을 관심영역(ROI)으로 저장함.
#cv2.rectangle(roi, (0,0), (rows-5, cols-1), (0,255,0))
print(rows)
print(cols)
print(channels)

#gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY) #로고파일의 색상을 그레이로 변경
####ret, mask = cv2.threshold(src2, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경
#mask_inv = cv2.bitwise_not(mask) #배경 검정, 로고 흰색

fgbg = cv2.createBackgroundSubtractorMOG2()

frame = src2.copy()
frame = cv2.resize(frame, (50, 50))
fgmask = fgbg.apply(frame)
cv2.imshow('original', frame)
cv2.imshow('MOG', fgmask)

#dst = cv2.bitwise_not(fgmask)
#cv2.imshow('dst', dst)  
#cv2.imwrite('./testImg/noBg1.jpg', dst)  

roi = src1[0:rows, 0:cols]

#dst = cv2.bitwise_or(src1, mask)
#dst2 = cv2.bitwise_or(src2_fg, src3_fg)
#cv2.imshow('dst2', dst2)
 
#src1[30:rows+30,30:cols+30] = src2 #src1에 src2값 합성
#img1 = src1.copy()

#dst = cv2.addWeighted(roi, 0, src2, 1, 0)
#dst = cv2.add(roi, img)
#dst = cv2.bitwise_and(img, src1)
#src1[0:rows, 0:cols] = dst
#img1[30:rows + 30+30, 30:cols +60] = src3
 
#cv2.imshow('result',)
img = Image.open('./testImg/No1.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
cutoff = 100

for item in datas:
    if item[0] >= cutoff and item[1] >= cutoff and item[2] >= cutoff:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("./testImg/new.png", "PNG")

img1 = cv2.imread('./testImg/new.png')

#dst = cv2.addWeighted(roi, 0, img1, 1, 0)
#src1[30:rows+30,30:cols+30] = img1
#dst = cv2.add(roi, img1)
src1[0:rows, 0:cols] = img1
cv2.imshow("dst", src1)

mask = np.full_like(img1, 255)
height, width = src1.shape[:2]
center = (width//2, height//2)

mix = cv2.seamlessClone(img1, src1, mask, center, cv2.MIXED_CLONE)
cv2.imshow('mix', mix)
cv2.waitKeyEx()
cv2.destroyAllWindows()