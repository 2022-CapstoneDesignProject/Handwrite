#from potrace import Bitmap

#bitmap = Bitmap(data)
#path = bitmap.trace()

#Code to convert png to svg
import matplotlib.pyplot as plt

x = plt.imread('./newImg/combin1.png')[..., 0]
image_format = 'svg' 
x.shape
plt.imsave('./newImg/1.svg', x, format='svg', cmap='gray')

#x = plt.imread('./newImg/1.svg')[..., 0]
#plt.imshow(x, cmap='gray')

# <2nd Solution>
# This code example demonstrates how to convert PNG to SVG
#import aspose.words as aw

#  Create document object
#doc = aw.Document()

# Create a document builder object
#builder = aw.DocumentBuilder(doc)

# Load and insert PNG image
#shape = builder.insert_image("./newImg/1.png")

# Specify image save format as SVG
#saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)

# Save image as SVG
#shape.get_shape_renderer().save("./newImg/svg1.svg", saveOptions)