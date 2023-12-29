import cv2
import numpy as np

def get_neighbourhood(image, i, j, radius):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Get the neighbourhood of the pixel
    neighbourhood = image[max(i - radius, 0):min(i + radius + 1, height),
                          max(j - radius, 0):min(j + radius + 1, width)]

    return neighbourhood


def apply_kuwahara(neighbourhood, method):
    # Get the dimensions of the neighbourhood
    height, width, _ = neighbourhood.shape

    # Get the four sub-neighbourhoods
    sub_neighbourhoods = [neighbourhood[:height // 2, :width // 2],
                          neighbourhood[:height // 2, width // 2:],
                          neighbourhood[height // 2:, :width // 2],
                          neighbourhood[height // 2:, width // 2:]]

    # Apply the kuwahara filter
    if method == 'gaussian':
        sub_neighbourhoods = [cv2.GaussianBlur(sub_neighbourhood, (5, 5), 0) for sub_neighbourhood in sub_neighbourhoods]
    elif method == 'median':
        sub_neighbourhoods = [cv2.medianBlur(sub_neighbourhood, 5) for sub_neighbourhood in sub_neighbourhoods]
    else:
        raise ValueError('Invalid method')

    # Get the variance of each sub-neighbourhood
    variances = [np.var(sub_neighbourhood) for sub_neighbourhood in sub_neighbourhoods]

    # Get the index of the sub-neighbourhood with the minimum variance
    min_variance_index = variances.index(min(variances))

    # Get the filtered pixel
    filtered_pixel = np.mean(sub_neighbourhoods[min_variance_index])

    return filtered_pixel


def generalized_kuwahara(image, method, radius):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Create a copy of the image
    filtered_image = image.copy()

    # Iterate over each pixel in the image
    for i in range(height):
        for j in range(width):
            # Get the pixel values in the neighbourhood of the pixel
            neighbourhood = get_neighbourhood(image, i, j, radius)

            # Apply the kuwahara filter
            filtered_pixel = apply_kuwahara(neighbourhood, method)

            # Update the pixel value in the filtered image
            filtered_image[i, j] = filtered_pixel

    return filtered_image