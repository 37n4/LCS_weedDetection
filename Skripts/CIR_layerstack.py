import cv2
import numpy as np

#-------------------------for LCC images----------------------------------------------------

for i in range(x, y):


    imread_ir = cv2.imread("/path/to/input/ir/images/" + str(i) + "_aligned.jpg")
    imread_rgb = cv2.imread("/path/to/input/rgb/images/" + str(i) + ".jpg")
    B , G , R  = cv2.split(imread_rgb)
    ir = imread_ir[:, :, 1]

    irgr = cv2.merge([ir,G,R]) # in GIS: Kanal 1 rot, Kanal 2 grün, Kanal 3 infrarot

    cv2.imwrite("/path/to/output/layerstack/" + str(i)+ ".jpg", irgr, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print(i)

