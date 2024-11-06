from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def save_image(array, filename):
    image = Image.fromarray(array)
    image.save(filename, format='PNG')

def structuring_element(size=3):
    return np.ones((size, size), dtype=np.uint8)

#def erode_rgb(image, kernel):
#    r_ch, g_ch, b_ch = image[:,:,0], image[:,:,1], image[:,:,2]
#    red = erode_single_ch(r_ch, kernel)
#    green = erode_single_ch(g_ch, kernel)
#    blue = erode_single_ch(b_ch, kernel)
#
#    eroded_image = np.stack((red, green, blue), axis=2)
#    return eroded_image

def erosi(image, kernel):
    k_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
    hasilErosi = np.zeros_like(image)

    for i in range(k_center[0], image.shape[0] - k_center[0]):
        for j in range(k_center[1], image.shape[1] - k_center[1]):
            if np.all(image[i - k_center[0]:i + k_center[0] + 1, j - k_center[1]:j + k_center[1] + 1] & kernel):
                hasilErosi[i,j] = 255
    return hasilErosi

def dilate(image, kernel):
    k_center = (kernel.shape[0] // 2, kernel.shape[1] // 2)
    dilated = np.zeros_like(image)

    for i in range(k_center[0], image.shape[0] - k_center[0]):
        for j in range(k_center[1], image.shape[1] - k_center[1]):
            if np.any(image[i - k_center[0]:i + k_center[0] + 1, j - k_center[1]:j + k_center[1] + 1] & kernel):
                dilated[i,j] = 255

    print(image.shape[0])
    print(image.shape[1])
    return dilated

def opening(image, kernel):
    dilate(erosi(image, kernel), kernel)

def closing(image, kernel):
    erosi(dilate(image, kernel), kernel)

kernel = structuring_element()
image = Image.open("/home/nicolaus/DataspellProjects/Image_Processing/Morfologi Citra/citra partitur notasi angka.png")
npar = np.array(image)
hasil = erosi(npar, kernel)
save_image(hasil, "hasil erosi.png")
