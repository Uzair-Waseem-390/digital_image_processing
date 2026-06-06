# Experiment 1.1: Read and Display Color Image with OpenCV


import cv2

img = cv2.imread('images/uzair.png')

cv2.imshow('window_name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Experiment 1.2: Read with OpenCV, Display as Grayscale with OpenCV
import cv2
img_gray = cv2.imread('images/uzair.png', 0)   # 0 for gray scale, 1 for color, -1 for unchanged
cv2.imshow('gray_scale_image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Experiment 1.3: Read with OpenCV, Display with Matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/uzair.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # CONVERSION is KEY!
plt.imshow(img_rgb)
plt.show()


# Experiment 1.4: Read Color Image with OpenCV, Display as Grayscale with Matplotlib

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/uzair.png', 0)  # Read as grayscale
plt.imshow(img, cmap='gray')  # cmap='gray' is IMPORTANT!
plt.show()


import cv2
import matplotlib.pyplot as plt
#Step 1: Reading the image
img=cv2.imread('images/uzair.png')
#Step 2: Converting the image to RGB format
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Step 3: Displaying the image using matplotlib
plt.subplot(1,2,1),plt.imshow(img),
plt.title('Input image'),plt.axis('off')
plt.subplot(1,2,2),plt.imshow(image),
plt.title('RGB format'),plt.axis('off')
plt.tight_layout()
plt.show()


# # Experiment 1.5: Read and Display Using Matplotlib Only
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('images/uzair.png')
plt.imshow(img)
plt.show()


# # Experiment 1.6: Read and Display Using Pillow

from PIL import Image

img = Image.open('images/uzair.png')
img.show()


# Experiment 1.7: Read and Display Using Scikit-image
from skimage import io

img = io.imread('images/uzair.png')
io.imshow(img)
io.show()