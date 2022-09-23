from lib2to3.pytree import convert
import cv2
import numpy as np
from PIL import Image

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 

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

mask = np.full_like(img1, 255)
height, width = src1.shape[:2]
center = (width//2, height//2)

normal = cv2.seamlessClone(img1, src1, mask, center, cv2.NORMAL_CLONE)
cv2.imshow('mix', normal)

cv2.waitKeyEx()
cv2.destroyAllWindows()
