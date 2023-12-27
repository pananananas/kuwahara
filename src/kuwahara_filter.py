import cv2
import numpy as np

def kuwahara_filter(image, kernel_size=5):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    height, width = gray_image.shape
    print(height,width)

    # Create a copy of the image
    filtered_image = np.copy(gray_image)

    # Iterate over each pixel in the image
    for i in range(height - kernel_size):
        for j in range(width - kernel_size):
            # print(i,j)
            # Get the mean and variance of the 4 regions
            mean = []
            variance = []
            for k in range(4):
                region = gray_image[i:i + kernel_size, j:j + kernel_size]
                mean.append(np.mean(region))
                variance.append(np.var(region))

            # Get the index of the region with the minimum variance
            min_variance_index = variance.index(min(variance))

            # Set the value of the pixel to the mean of the region with the minimum variance
            filtered_image[i, j] = mean[min_variance_index]

    return filtered_image