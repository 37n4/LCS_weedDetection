import cv2
import numpy as np
from PIL import Image


#---------------------------for low Cost Camera---------------------------------------------------------------
for i in range(x, y):

    imread_irgr = cv2.imread("/path/to/CIR/layerstacks/" + str(i)+ ".jpg")

  
    def calc_ndvi(ir_image):
        
        ir, r, g = cv2.split(ir_image)
        #B, G ,R = cv2.split(rgb_image)

        bottom = (ir.astype(float) + r.astype(float))
        bottom[bottom==0] = 0.01
        ndvi = (ir.astype(float) - r) / bottom
        return ndvi

    def contrast_stretch(im):
        in_min = np.percentile(im, 5)
        in_max = np.percentile(im, 95)
        out_min = 0.0
        out_max = 255.0
        
        out = im - in_min
        out *= ((out_min - out_max) / (in_min - in_max))
        out += in_min

        return out

    ndvi = calc_ndvi(imread_irgr)
    ndvi = contrast_stretch(ndvi)
    ndvi = cv2.normalize(ndvi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    cv2.imwrite("/path/to/NDVI/output" + str(i)+ ".jpg", n
    ndvi, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print(i)



#-------------------------------------for altum camera-----------------------------------------------------------------------

for i in range(0, 71):

    #irgr Fotos not cropped!
    imread_irgr = cv2.imread("/Volumes/SSD/Fotos_Studienprojekt_2022/Altum/0727_MaisAnna/Altum/0010SET/aligned2_cropped/" + str(i)+ "_cropped.png")

    #GDVI = (NIR - GREEN) / (NIR + GREEN)
    def calc_gdvi(ir_image):
        
        g, r, ir = cv2.split(ir_image)
        #B, G ,R = cv2.split(rgb_image)

        bottom = (ir.astype(float) + r.astype(float))
        bottom[bottom==0] = 0.01
        gdvi = (ir.astype(float) - r) / bottom
        return gdvi

    def contrast_stretch(im):
        in_min = np.percentile(im, 5)
        in_max = np.percentile(im, 95)
        out_min = 0.0
        out_max = 255.0
        
        out = im - in_min
        out *= ((out_min - out_max) / (in_min - in_max))
        out += in_min

        return out

    gdvi = calc_gdvi(imread_irgr)
    gdvi = contrast_stretch(gdvi)
    gdvi = cv2.normalize(gdvi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    cv2.imwrite("/Volumes/SSD/Fotos_Studienprojekt_2022/Altum/0727_MaisAnna/Altum/0010SET/GDVI/" + str(i)+ ".png", gdvi)
    print(i)


#----------------------------------------Threshold--------------------------------------------------------------------

for i in range(x,y):

    ndvi = cv2.imread("/path/to/images/" + str(i)+ ".png", cv2.IMREAD_GRAYSCALE)

    ndvi_blurred = cv2.GaussianBlur(ndvi, (7, 7), 0)
    thresh_ndvi = cv2.adaptiveThreshold(ndvi_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 255, 5 )

    cv2.imwrite("path/to/output/images/" + str(i)+ ".png", thresh_ndvi)
    print(i)