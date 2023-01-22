import os, argparse
import cv2
import numpy as np
from numpy.fft import fft2, ifft2, fftshift


def find_transform(im_src, im_dst):
    warp = np.eye(3, dtype=np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 0.001)
    try:
        _, warp = cv.findTransformECC(im_src, im_dst, warp, cv.MOTION_HOMOGRAPHY, criteria)
    except:
        print('Warning: find transform failed. Set warp as identity')
    return warp



def eccAlign(im1,im2):
    
    # Convert images to grayscale
    bildname1 = "/Volumes/SSD/Fotos_Studienprojekt_2022/Pi1_Sept/1/" + str(i) + ".jpg"
    bildname2 = "/Volumes/SSD/Fotos_Studienprojekt_2022/Pi2_Sept/1/" + str(i) + ".jpg"
    im1 =  cv2.imread(bildname1)
    im2 =  cv2.imread(bildname2)
    im1_gray = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
    im2_gray = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

    # Find size of image1
    sz = im1.shape

    # Define the motion model
    warp_mode = cv2.MOTION_AFFINE

    # Define 2x3 or 3x3 matrices and initialize the matrix to identity
    if warp_mode == cv2.MOTION_HOMOGRAPHY :
        warp_matrix = np.eye(3, 3, dtype=np.float32)
    else:
        warp_matrix = np.eye(2, 3, dtype=np.float32)

    # Define termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
     1000, 1e-5)

    # Run the ECC algorithm. The results are stored in warp_matrix.
    #warp = find_transform(im1_gray, im2_gray)
    (cc, warp_matrix) = cv2.findTransformECC(im1_gray, im2_gray, warp_matrix, warp_mode, criteria, None, 5)

    if warp_mode == cv2.MOTION_HOMOGRAPHY :
        # Use warpPerspective for Homography 
        im2_aligned = cv2.warpPerspective (im2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    else :
        # Use warpAffine for Translation, Euclidean and Affine
        im2_aligned = cv2.warpAffine(im2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);

    return im2_aligned, warp_matrix

for i in range(53, 1101):
    print(i)
    try:
        aligned, warp_matrix = eccAlign("/Volumes/SSD/Fotos_Studienprojekt_2022/Pi1_Sept/1/" + str(i) + ".jpg", "/Volumes/SSD/Fotos_Studienprojekt_2022/Pi2_Sept/1/" + str(i) + ".jpg")
    except Exception as e:
        print("Error occured:" + str(i))
        continue
    cv2.imwrite("/Volumes/SSD/Fotos_Studienprojekt_2022/Pi2_Sept/1_aligned/" + str(i) + "_aligned.jpg" ,aligned, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print(i)
