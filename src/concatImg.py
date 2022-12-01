import os
import random
from PIL import Image, ImageOps


def concat_images(image_paths, size, shape=None):

    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)
   
    images = [ImageOps.fit(image, size, Image.ANTIALIAS) 
              for image in images]
    
    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    image = Image.new('RGB', image_size)
    
    idx = 0
    # Paste images into final image
    for row in range(shape[0]): 
        for col in range(shape[1]):    
               
            offset = width * col, height * row
            #print(offset)
            #idx = row * shape[1] + col
            #print(idx)
            image.paste(images[idx], offset)
            idx  = idx + 1
    
    return image

