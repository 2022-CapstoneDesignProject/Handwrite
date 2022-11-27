import imutils
import cv2
import numpy as np
import os
from PIL import Image
import sys

#사용자가 업로드한 이미지 중 가장 최근 이미지 가져오기
files_path = "../web/uploads/"
filename_time = []

for f_name in os.listdir(files_path):
	each_path = files_path + f_name
	time = os.path.getctime(each_path)
	filename_time.append((each_path, time))

recent_file = max(filename_time, key = lambda x:x[1])[0]
#image = cv2.imread("./newImg/newTemplate1.png")
image = cv2.imread(recent_file)
#cv2.imshow('img',image)
image_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
image_gray_blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)

ret,thresh2 = cv2.threshold(image_gray,160,255,cv2.THRESH_BINARY)

#cv2.imshow('thresh2',thresh2)


# 모양을 구분해주는 ShapeDetector
class ShapeDetector:	
	def __init__(self):		
		pass

	def detect(self, c):	
		# initialize the shape name and approximate the contour		
		shape = "unidentified"		
		peri = cv2.arcLength(c, True)		
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)		
		# if the shape is a triangle, it will have 3 vertices		
		if len(approx) == 3:			
			shape = "triangle"				
		# if the shape has 4 vertices, it is either a square or		
		# # a rectangle		
		elif len(approx) == 4:		
			# compute the bounding box of the contour and use the			
			# # bounding box to compute the aspect ratio			
			(x, y, w, h) = cv2.boundingRect(approx)			
			ar = w / float(h)					
			
			# a square will have an aspect ratio that is approximately			
			# # equal to one, otherwise, the shape is a rectangle	
			#if ar >= 0.95 and ar <= 1.05 :		
			#	shape = "square"  
			#else :
			shape = "rectangle"				
			# if the shape is a pentagon, it will have 5 vertices		
		elif len(approx) == 5:			
			shape = "pentagon"				
			# otherwise, we assume the shape is a circle		
		else:			
			shape = "circle"				
			# return the name of the shape		
		return shape

def detectRec() :
	sd = ShapeDetector() 
	#cnts = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
	cnts = cv2.findContours(thresh2.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
	cnts = cnts[0] #if imutils.is_cv2() else cnts[1]

	contours1_img = cv2.drawContours(thresh2, cnts, -1, (0, 255, 0), 3)
	#cv2.imshow('contours1_img', contours1_img)

	contours_xy = np.array(cnts)
	contours_xy.shape


	#count = 0
	count = 41
	for c in cnts:

		if sd.detect(c) != 'rectangle': 
			next
		print(sd.detect(c))

		c = c.astype("float")

		c = c.astype("int")

		x,y,w,h = cv2.boundingRect(c)

		print(w)
		print(h)

		#cv2.rectangle(thresh2,(x,y),(x+w,y+h),(3,255,4),2)

		#cv2.imshow("image", image)

		#cv2.waitKey(0)

		if not (85 < w < 95 and 85 < h < 95): 
			print("skip" + str(w) + " - " + str(h))
			continue

		count = count-1

		cv2.imwrite("./crop/"+str(count)+".png", image[y: y + h, x: x + w])



cv2.waitKeyEx()
cv2.destroyAllWindows()

path = './crop'
if not os.path.isdir(path):
	os.makedirs(path)

detectRec()
