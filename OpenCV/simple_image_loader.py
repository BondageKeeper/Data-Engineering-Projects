import numpy as np
def image_loader(path,nx,ny):
    image = cv2.imread(path,0)
    binary_data = None
    if image is None:
        exit()
    else:
        height , width = image.shape
        center_pixel_color = image[height // 2,width // 2]
        image_resized = cv2.resize(image,(nx,ny))
        print(center_pixel_color)
        if center_pixel_color > 127: #object is white and background is relatively black
            _ , binary_data = cv2.threshold(image_resized,127,1,cv2.THRESH_BINARY)
            print('condition if')
        else:
            _ , binary_data = cv2.threshold(image_resized,127,1,cv2.THRESH_BINARY_INV)
            print('condition else')
        binary_data = cv2.flip(binary_data,0)
    return binary_data.astype(np.bool)

image_loader('wing_two.png',300,300)
