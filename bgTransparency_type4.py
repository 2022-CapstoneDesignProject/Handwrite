from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기
src2 = cv2.imread('./testimg/No1.jpg') 

for j in range(10,15):
    for i in range(1,23):
        img = Image.open('./testImg/jamo/backgroundO/letter'+str(i)+'_'+str(j)+'.png')
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        cutoff = 150

        for item in datas:
            if item[0] >= cutoff and item[1] >= cutoff and item[2] >= cutoff:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save("./testImg/jamo/backgroundX/letter"+str(i)+'_'+str(j)+".png", "PNG")


cv2.waitKeyEx()
cv2.destroyAllWindows()