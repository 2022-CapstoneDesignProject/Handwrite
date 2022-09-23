#글자만 추출

from PIL import Image
for i in range(1,5):
    img = Image.open('./testImg/'+str(i)+'.png')
    #im.save(str(i)+'.png')
    #img = Image.open(str(i)+'.png')
    img = img.convert("RGBA")
    datas =img.getdata()
    newData = []
    cutOff = 100
    

    for item in datas:
        if item[0] > cutOff and item[1] > cutOff and item[2] > cutOff:
            newData.append((150, 25, 255, 0))
#             RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿔줍니다.

        else:
            newData.append(item)
        
    img.putdata(newData)
    img.save('./testImg/'+str(i)+'_Extract.png', "PNG")
