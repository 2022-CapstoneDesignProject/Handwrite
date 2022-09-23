from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 

#이미지 배경 투명하게 만들기
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

#자음, 모음 한 글자로 합치기
img1 = cv2.imread('./testImg/new.png')
img2 = cv2.imread('./testImg/No2.jpg')

mask = np.full_like(img1, 255)
height, width = src1.shape[:2]
center = (width//3, height//3)

normal = cv2.seamlessClone(img1, src1, mask, center, cv2.NORMAL_CLONE)

rows, cols, channels = img2.shape
normal[50:rows+50,200:cols+200] = img2
cv2.imshow('mix', normal)

cv2.waitKeyEx()
cv2.destroyAllWindows()
