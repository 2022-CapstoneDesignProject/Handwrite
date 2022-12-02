
import bgTransparency
import jamoComb1
import jamoComb2
import jamoComb3
import jamoComb4
import jamoComb5
import jamoComb6
import jamoComb7
import jamoComb8
import jamoComb9
import concatImg
import pngtottf
import os
from PIL import Image, ImageOps
#import web.cropRect as cropRect

if __name__=="__main__":
    jamoComb1.jamoComb1()
    jamoComb2.jamoComb2()
    jamoComb3.jamoComb3()
    jamoComb4.jamoComb4()
    jamoComb5.jamoComb5()
    jamoComb6.jamoComb6()
    jamoComb7.jamoComb7()
    jamoComb8.jamoComb8()
    jamoComb9.jamoComb9()
    #rmMargin.removeMargin()
    #bgTransparency.bgTransparency()
    # Get list of image paths
    folder = '../web/comb'

    image_paths = [os.path.join(folder, f) 
                for f in os.listdir(folder) if f.endswith('.png')]

    # Random selection of images
    #image_array = random.choices(image_paths, k=8)

    # Create and save image grid
    #image = concat_images(image_paths, (30, 30), (56, 76))
    image = concatImg.concat_images(image_paths, (100, 100), (84, 133))
    path = './concat'
    if not os.path.exists(path):
        os.makedirs(path)
    image.save(path+'/image.png', 'PNG')

    pngtottf.makefont()
    print("Successful")