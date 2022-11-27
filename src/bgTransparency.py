from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image
import os

def bgTransparency() :

    #directory 존재하지 않은 경우 생성
    path = './cropImg/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    for j in range(1,57):
        img = Image.open('./cropImg/letter'+str(j)+'.png')
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
        img.save(path+'/letter'+str(j)+".png", "PNG")

    cv2.waitKeyEx()
    cv2.destroyAllWindows()