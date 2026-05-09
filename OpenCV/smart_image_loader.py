import numpy as np
import cv2
def smart_otsu_loader(path,nx,ny):
    image2 = cv2.imread(path,0)
    if image2 is None:
        exit()
    else:
        image2 = cv2.resize(image2,(nx,ny))
        _ , binary_value = cv2.threshold(image2,0,1,cv2.THRESH_BINARY + cv2.THRESH_OTSU) #0 - not used but we write it!
    if np.sum(binary_value) > (nx * ny) / 2:
        binary_value = 1 - binary_value
        print('emited!')
    binary_value = cv2.flip(binary_value,0)
    return binary_value.astype(np.bool)
smart_otsu_loader('Clark_wing.png',300,300)
