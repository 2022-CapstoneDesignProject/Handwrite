from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

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
        cutoff = 150

        for item in datas:
            if item[0] >= cutoff and item[1] >= cutoff and item[2] >= cutoff:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(img_dir+str(i)+'.png', "PNG")
        i += 1

def bgTransparency1() :

    #directory 존재하지 않은 경우 생성
    path = './testImg/jamo/backgroundX'
    if not os.path.exists(path):
        os.makedirs(path)
    
    for j in range(1,10):
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
            img.save(path+'/letter'+str(i)+'_'+str(j)+".png", "PNG")


    cv2.waitKeyEx()
    cv2.destroyAllWindows()