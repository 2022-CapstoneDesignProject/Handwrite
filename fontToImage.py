
import sys
import os
import subprocess

from fontTools.ttLib import TTFont

TEXTS_DIR = "texts"
IMAGES_DIR = "images"
print(sys.argv)
TTF_PATH = sys.argv[1]
FONT_SIZE = sys.argv[2]
TTF_NAME, TTF_EXT = os.path.splitext(os.path.basename(TTF_PATH))

ttf = TTFont(TTF_PATH, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)

for d in [TEXTS_DIR, IMAGES_DIR]:
    if not os.path.isdir(d):
        os.mkdir(d)

for x in ttf["cmap"].tables:
    for y in x.cmap.items():
        char_unicode = chr(y[0])
        char_utf8 = char_unicode.encode('utf_8')
        char_name = y[1]
        f = open(os.path.join(TEXTS_DIR, char_name + '.txt'), 'wb')
        f.write(char_utf8)
        f.close()
ttf.close()

files = os.listdir(TEXTS_DIR)
for filename in files:
    name, ext = os.path.splitext(filename)
    input_txt = TEXTS_DIR + "/" + filename
    output_png = IMAGES_DIR + "/" + TTF_NAME + "_" + name + "_" + FONT_SIZE + ".png"
    print("convert", "-font", TTF_PATH, "-pointsize", FONT_SIZE, "-background", "rgba(0,0,0,0)", "label:@" + input_txt, output_png)
    sys.exit()
    subprocess.call(["convert", "-font", TTF_PATH, "-pointsize", FONT_SIZE, "-background", "rgba(0,0,0,0)", "label:@" + input_txt, output_png])
    
print("finished")


""", osconvert -sample 176x144"""
"""
import sys, os 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

#font_name = 'C:/Windows/Fonts/arial.ttf'
#font_family = font_manager.FontProperties(fname = font_name).get_name()
#plt.rcParams["font.family"] = font_family

from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

font_path = "./font"
fonts = os.listdir("./font")

#fnt = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)

co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
start = "AC00"
end = "D7A3"

co = co.split(" ")

Hangul_Syllables = [a+b+c+d 
                    for a in co 
                    for b in co 
                    for c in co 
                    for d in co]

Hangul_Syllables = np.array(Hangul_Syllables)

s = np.where(start == Hangul_Syllables)[0][0]
e = np.where(end == Hangul_Syllables)[0][0]

Hangul_Syllables = Hangul_Syllables[s : e + 1]

unicodeChars = chr(int(Hangul_Syllables[0], 16))

plt.figure(figsize=(15, 15))

for idx, ttf in enumerate(fonts):

    font = ImageFont.truetype(font = font_path + ttf, size = 100)

    x, y = font.getsize(unicodeChars)

    theImage = Image.new('RGB', (x + 3, y + 3), color='white')

    theDrawPad = ImageDraw.Draw(theImage)

    theDrawPad.text((0, 0), unicodeChars[0], font=font, fill='black')

    plt.subplot("24{}".format(str(idx + 1)))
    
    plt.title(str(ttf))
    
    plt.imshow(theImage)
    
plt.show()

for uni in tqdm(Hangul_Syllables):
    
    unicodeChars = chr(int(uni, 16))
    
    path = "./Hangul_Syllables/" + unicodeChars
    
    os.makedirs(path, exist_ok = True)
        
    for ttf in fonts:
        
        font = ImageFont.truetype(font = font_path + ttf, size = 100)
        
        x, y = font.getsize(unicodeChars)
        
        theImage = Image.new('RGB', (x + 3, y + 3), color='white')
        
        theDrawPad = ImageDraw.Draw(theImage)
        
        theDrawPad.text((0.0, 0.0), unicodeChars[0], font=font, fill='black' )
        
        msg = path + "/" + ttf[:-4] + "_" + unicodeChars
        
        theImage.save('{}.png'.format(msg))
"""