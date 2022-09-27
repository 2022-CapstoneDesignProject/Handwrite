from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기
src2 = cv2.imread('./testimg/No1.jpg') 

#이미지 배경 투명하게 만들기
def imgTransparency(img_dir) :
    os.chdir(img_dir) #해당 폴더로 이동
    files = os.listdir(img_dir) #해당 폴더에 있는 파일 이름을 리스트 형태로 받음

    png_img = []
    jpg_img = []

    for img in files :
        if'.png' in img:
            i = 10
            f = cv2.imread(img)
            png_img.append(f)
        img = Image.open(img)
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
        img.save(img_dir+str(i)+'.png', "PNG")
        i += 1

img = Image.open('./testImg/combi.png')
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
img.save("./testImg/newcombi.png", "PNG")


cv2.waitKeyEx()
cv2.destroyAllWindows()