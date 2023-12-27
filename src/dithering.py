import cv2
import numpy as np


def ordered_dithering(image, dithering_matrix = 255 * np.array([[0, 8, 2, 10],
                                                                [12, 4, 14, 6],
                                                                [3, 11, 1, 9],
                                                                [15, 7, 13, 5]]) / 16):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            old_pixel = image[i, j]
            new_pixel = dithering_matrix[i % 4, j % 4]
            image[i, j] = [255 if old_pixel[k] > new_pixel else 0 for k in range(3)]

    return image


# change the bits of the image to the given number of bits
def quantization(image, bits):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            old_pixel = image[i, j]
            new_pixel = [int((old_pixel[k] / 255) * ((2 ** bits) - 1)) for k in range(3)]
            image[i, j] = [int((new_pixel[k] / ((2 ** bits) - 1)) * 255) for k in range(3)]

    return image