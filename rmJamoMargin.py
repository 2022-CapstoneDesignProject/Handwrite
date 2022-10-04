import sys, cv2
from matplotlib import pyplot as plt
import numpy as np

src1 = cv2.imread('./testImg/background2.png') #배경파일 읽기 
src2 = cv2.imread('./testImg/1.png') #ㄱ파일 읽기
src3 = cv2.imread('./testImg/2.png') #ㅏ파일 읽기
#src2Gray = cv2.imread('./testImg/1.png', cv2.IMREAD_GRAYSCALE)
src2Gray = cv2.cvtColor(src2, cv2.COLOR_RGB2GRAY)
#ret, src2mask = cv2.threshold(src2Gray, 160, 255, cv2.THRESH_BINARY) #배경은 흰색으로, 그림을 검정색으로 변경

#cv2.imshow('img1', src2)

blur = cv2.GaussianBlur(src2Gray, ksize=(5, 5), sigmaX=0)
ret, src2mask = cv2.threshold(blur, 160, 255, cv2.THRESH_BINARY)
src2Binary = cv2.bitwise_not(src2mask)

edged1 = cv2.Canny(blur, 10, 250)
#cv2.imshow('edged1', edged1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged1, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('closed', closed)

contours1, _ = cv2.findContours(closed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
total = 0

#외곽선 그리는 용도. 이미지에 그리기때문에 원래 이미지에 초록색 선이 생긴다.
#contours1_img = cv2.drawContours(src2, contours1, -1, (0, 255, 0), 3)
#cv2.imshow('contours1_img', contours1_img)

#외곽을 저장하고 있는 contours는 외곽의 점들이 모여 선을 나타내므로 각 점의 좌표를 가지고 있다
#리스트를 넘파이 array로 바꾸어 형태를 알아본다.
#contours[] : 물체가 몇개인지 // contours[][] : 각 좌표 // contours[][][x][y] : 세번째와 네번째부터는 각각 x축과 y축을 나타냄
contours_xy = np.array(contours1)
contours_xy.shape

x_min, x_max = 0, 0
value = list()

for i in range(len(contours_xy)):
    for j in range(len(contours_xy[i])):
        value.append(contours_xy[i][j][0][0]) #4번째 괄호가 0일때 x의 값
        x_min = min(value)-5
        x_max = max(value)+5

#print(x_min)
#print(x_max)

y_min, y_max = 0, 0
value = list()
for i in range(len(contours_xy)):
    for j in range(len(contours_xy[i])):
        value.append(contours_xy[i][j][0][1]) 
        y_min = min(value)-5
        y_max = max(value)+5

#print(y_min)
#print(y_max)

#imgae trim
x = x_min
y = y_min
w = x_max-x_min
h = y_max-y_min
img_trim = closed[y:y+h, x:x+w]
#cv2.imwrite('./testImg/No1.jpg', img_trim)
#org_img1 = cv2.imread('./testImg/No1.jpg')

#cv2.imshow('img_trim', img_trim)

#gray = cv2.cvtColor(org_img1, cv2.COLOR_BGR2GRAY)
ret, No1mask = cv2.threshold(img_trim, 160, 255, cv2.THRESH_BINARY_INV) #배경은 흰색으로, 그림을 검정색으로 변경
cv2.imshow('no1Mask', No1mask)
cv2.imwrite('./testImg/No1.jpg', No1mask)

org_img1 = cv2.imread('./testImg/No1.jpg')

cv2.waitKeyEx()
cv2.destroyAllWindows()
