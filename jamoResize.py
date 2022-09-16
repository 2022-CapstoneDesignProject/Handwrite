#자음, 모음 가로세로 비율 조정
#가로 비율은 fx 값 변경, 세로 비율은 fy값 변경
import cv2

img = cv2.imread("./testImg/2.png")
resize_img = cv2.resize(img,dsize=(0, 0),fx=0.5, fy=0.8)

cv2.imshow("img", img)
cv2.imshow("resize img", resize_img)
cv2.waitKey()
