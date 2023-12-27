import cv2
import numpy as np


def ordered_dithering(image, dithering_matrix = 255 * np.array([[0, 8, 2, 10],
                                                                [12, 4, 14, 6],
                                                                [3, 11, 1, 9],
                                                                [15, 7, 13, 5]]) / 16):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    height, width = gray_image.shape

    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            old_pixel = gray_image[i, j]
            new_pixel = dithering_matrix[i % 4, j % 4]
            gray_image[i, j] = 255 if old_pixel > new_pixel else 0

    return gray_image