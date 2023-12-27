import cv2
import numpy as np
from pykuwahara import kuwahara

import cv2
import numpy as np

image_path = 'las.jpg'  # Replace with your image path
image = cv2.imread(image_path)
if image is None:
    raise ValueError("Image not found")

# resize the image
image = cv2.resize(image, (1024, 1024))


filtered_image = kuwahara(image, method='gaussian', radius=5)    


# Display the original and filtered image
# cv2.imshow('Original Image', image)
cv2.imshow('Kuwahara Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save the filtered image
cv2.imwrite('filtered_image.jpg', filtered_image)