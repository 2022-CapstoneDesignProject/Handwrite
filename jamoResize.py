#자음, 모음 가로세로 비율 조정
#가로 비율은 fx 값 변경, 세로 비율은 fy값 변경
import cv2
from PIL import Image

#자음 크기조정
for i in range(1,20):
    img = Image.open('./cropImg/2/cropped/letter'+str(i)+'.png')
    resized_img=img
    if(img.width>60):
        resized_img = img.resize((60,img.height))
    if(img.height>60):
        resized_img = img.resize((img.width, 60))
    
    resized_img.save('./cropImg/2/cropped/resized/letter'+str(i)+'.png', "PNG")

#모음 크기조정
for i in range(20,28): #오른쪽 모음 width 45이내로 height 70 이내로
    img = Image.open('./cropImg/2/cropped/letter'+str(i)+'.png')
    resized_img=img
    if(img.width>45):
        resized_img = img.resize((45,img.height))
    if(img.height>70):
        resized_img = img.resize((img.width, 70))
    
    resized_img.save('./cropImg/2/cropped/resized/letter'+str(i)+'.png', "PNG")

for i in [28,32,33,37,38]: #아래쪽 모음 width 75이내로 height 40 이내로
    img = Image.open('./cropImg/2/cropped/letter'+str(i)+'.png')
    resized_img=img
    if(img.width>75):
        resized_img = img.resize((75,img.height))
    if(img.height>40):
        resized_img = img.resize((img.width, 40))
    
    resized_img.save('./cropImg/2/cropped/resized/letter'+str(i)+'.png', "PNG")

for i in [29,30,31,34,35,36,39]: #오른쪽+아래쪽 모음 width 80이내로 height 80 이내로
    img = Image.open('./cropImg/2/cropped/letter'+str(i)+'.png')
    resized_img=img
    if(img.width>80):
        resized_img = img.resize((80,img.height))
    if(img.height>80):
        resized_img = img.resize((img.width, 80))
    
    resized_img.save('./cropImg/2/cropped/resized/letter'+str(i)+'.png', "PNG")   

