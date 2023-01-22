import sys
import os
from PIL import Image
from PIL import ImageFile
from tifffile import tifffile

#---------------------------------Script for Altum images with original name----------------------------------------------

ImageFile.LOAD_TRUNCATED_IMAGES = True

filepath = "/path/to/Altum/input/images/"

for i in range(88,161):

    count = 10000 
    count = count + i
    count = str(count)
    count = count[1:]

    print(i)
    # Attempt to open an image file
    image = Image.open(os.path.join(filepath, "IMG_" + count + '_irgr_aligned.png'))

    # Perform operations on the image here
    image = image.crop((left, top, right, bottom))
    
    # Split our origional filename into name and extension 
    #name, extension = os.path.splitext(filename)

    # Save the image as "(origional_name)_thumb.jpg
    print(str(i) + '_cropped')
    image.save(os.path.join("/path/to/cropped/Altum/output/images/", str(i) + '_cropped.png'))

#------------------------------------------------------------------------------------------------------------------------------------------


ImageFile.LOAD_TRUNCATED_IMAGES = True

filepath = "/Users/annaseiche/Desktop/Index_Berechnung/Altum/009/ViGreen_Thresh"

for i in range(88,161):
    print(i)
    image = Image.open(os.path.join(filepath, str(i) + '.png'))
    image = image.crop((170, 120, 1330, 1030))
    image.save(os.path.join("/Users/annaseiche/Desktop/Index_Berechnung/Altum/009/mask/", str(i) +  '.png'))