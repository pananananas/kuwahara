import numpy as np
import cv2
from PIL import Image

_diffusion_matrices = {
    'bayer4x4': 1./17. * np.array([
        [ 1,  9,  3, 11],
        [13,  5, 15,  7],
        [ 4, 12,  2, 10],
        [16,  8, 14,  6]
    ]),
    'bayer8x8': 1./65. * np.array([
        [ 0, 48, 12, 60,  3, 51, 15, 63],
        [32, 16, 44, 28, 35, 19, 47, 31],
        [ 8, 56,  4, 52, 11, 59,  7, 55],
        [40, 24, 36, 20, 43, 27, 39, 23],
        [ 2, 50, 14, 62,  1, 49, 13, 61],
        [34, 18, 46, 30, 33, 17, 45, 29],
        [10, 58,  6, 54,  9, 57,  5, 53],
        [42, 26, 38, 22, 41, 25, 37, 21]
    ]),
    'cluster4x4': 1./15. * np.array([
        [12,  5,  6, 13],
        [ 4,  0,  1,  7],
        [11,  3,  2,  8],
        [15, 10,  9, 14]
    ]),
    'cluster8x8': 1./64. * np.array([
        [24, 10, 12, 26, 35, 47, 49, 37],
        [ 8,  0,  2, 14, 45, 59, 61, 51],
        [22,  6,  4, 16, 43, 57, 63, 53],
        [30, 20, 18, 28, 33, 41, 55, 39],
        [34, 46, 48, 36, 25, 11, 13, 27],
        [44, 58, 60, 50,  9,  1,  3, 15],
        [42, 56, 62, 52, 23,  7,  5, 17],
        [32, 40, 54, 38, 31, 21, 19, 29]
    ]),
}

# dithering using the given matrix
def ordered_dithering(image, matrix='bayer4x4'):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Get the diffusion matrix
    diffusion_matrix = _diffusion_matrices[matrix]

    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            old_pixel = image[i, j]
            new_pixel = [int((old_pixel[k] / 255) + diffusion_matrix[i % len(diffusion_matrix), j % len(diffusion_matrix)] - 0.5) * 255 for k in range(3)]
            image[i, j] = [int((new_pixel[k] / 255) * 255) for k in range(3)]

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