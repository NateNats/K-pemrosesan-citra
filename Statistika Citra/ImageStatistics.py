import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

class ImageStatistics:
    def __init__(self, image):
        self.math = math
        self.skewness_value = []
        self.np = np
        self.image = image
        self.pixel_val = 0
        self.mean = 0
        self.std_val = 0
        self.n_pixel = 0

    # def rgb2gray(self, image):
    #     height, width, _ = image.shape
    #     gray_image = [[0] * width for _ in range(height)]
    #
    #     for i in range(height):
    #         for j in range(width):
    #             r, g, b = image[i][j]
    #             gray_val = ((0.2989 * r) + (0.5870 * g) + (0.1140 * b))
    #             gray_image[i][j] = gray_val
    #
    #     return gray_image

    def flatten(self, array):
        return [titik for baris in array for titik in baris]

    def countMean(self, val):
        return np.mean(val)

    def countstd(self, val, mean):
        deviation_sum = sum((x - mean) ** 2 for x in val)
        return self.math.sqrt(deviation_sum / (len(val) - 1))

    def calculate_skew(self, pixel_val, mean, std_val):
        n_pixel = len(pixel_val)
        skewness = np.sum(((pixel_val - mean) / std_val) ** 3) / n_pixel
        return skewness

    def calculate_kurtosis(self, pixel_val, mean, std_val):
        n_pixel = len(pixel_val)
        kurtosis = np.sum(((pixel_val - mean) / std_val) ** 4) / n_pixel - 3
        return kurtosis

    def display_statistics(self):
        if len(self.image.shape) == 3 and self.image.shape[2] == 3:
            channels = cv2.split(self.image)
            stats = {'Channel': ['Red', 'Green', 'Blue'],
                     'Mean': [],
                     'Standard Deviation': [],
                     'Skewness': [],
                     'Kurtosis': []}

            for i, channel in enumerate(channels):
                pixel_val = np.array(self.flatten(channel))
                mean = self.countMean(pixel_val)
                std_val = self.countstd(pixel_val, mean)
                skewness = self.calculate_skew(pixel_val, mean, std_val)
                kurtosis = self.calculate_kurtosis(pixel_val, mean, std_val)

                stats['Mean'].append(mean)
                stats['Standard Deviation'].append(std_val)
                stats['Skewness'].append(skewness)
                stats['Kurtosis'].append(kurtosis)

                plt.subplot(1, 3, i+1)
                plt.hist(pixel_val, bins=256, color=['r', 'g', 'b'][i], alpha=0.7)
                plt.title(f"{stats['Channel'][i]} Channel")
                plt.xlabel('Pixel Intensity')
                plt.ylabel('Frequency')
                plt.grid(True)

                print(f"Statistics for {stats['Channel'][i]} Channel:")
                print(f"  Mean               : {stats['Mean'][i]:.2f}")
                print(f"  Standard Deviation : {stats['Standard Deviation'][i]:.2f}")
                print(f"  Skewness           : {stats['Skewness'][i]:.2f}")
                print(f"  Kurtosis           : {stats['Kurtosis'][i]:.2f}")
                print()

            plt.tight_layout()
            plt.show()

        else:
            raise ValueError("Gambarnya ga 3 channels masbro....")


image_path = 'gambar.jpg'
image = cv2.imread(image_path)

image_statistics = ImageStatistics(image)

image_statistics.display_statistics()

#%%
