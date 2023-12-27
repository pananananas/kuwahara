import cv2
import numpy as np
from pykuwahara import kuwahara
from dithering import ordered_dithering
from dithering import quantization

import cv2
import numpy as np

image_path = 'images/paper.jpg'  # Replace with your image path
image = cv2.imread(image_path)
if image is None:
    raise ValueError("Image not found")

# resize the image
image = cv2.resize(image, (1024, 1024))


filtered_image = quantization(image, 3)

filtered_image = kuwahara(filtered_image, method='gaussian', radius=5)    

# filtered_image = ordered_dithering(filtered_image)


# Display the original and filtered image
# cv2.imshow('Original Image', image)
cv2.imshow('Kuwahara Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

file_name = image_path.split('/')[-1].split('.')[0]
file_format = image_path.split('/')[-1].split('.')[1]

# Save the filtered image
cv2.imwrite('result/' + file_name + '_kuwahara.' + file_format, filtered_image)