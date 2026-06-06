# Experiment 1.8: Get Height and Width Using OpenCV

import cv2

img = cv2.imread('images/uzair.png')
height, width = img.shape[:2]  # ← KEY LINE!

print("Height:", height)
print("Width:", width)



# Experiment 1.9: Converting Color to Grayscale using OpenCV
import cv2

# resizing window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)    # resize able by user
cv2.namedWindow("Grayscale Image", cv2.WINDOW_AUTOSIZE) # not resizable but auto adjusts to image size

# Load image
img = cv2.imread('images/uzair.png')

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ← KEY LINE!

# Display original and grayscale images side-by-side
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Experiment 1.10: Changing Spatial Resolution (Downsampling)
"""
Downsampling: Downsampling is the process of reducing the number of pixels in an image, thereby reducing its spatial resolution.
In downsampling, we reduce the number of pixels in an image, which reduces its spatial resolution.
Example:
256×256  →  64×64  →  32×32  →  16×16
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/uzair.png', 0)  # Read as grayscale

# Downsampling - reducing spatial resolution
img1 = img                           # Original size
img2 = cv2.resize(img, (64, 64))     # 64×64
img3 = cv2.resize(img, (32, 32))     # 32×32
img4 = cv2.resize(img, (16, 16))     # 16×16

# Display all
plt.figure(figsize=(8,6))    # 8 is width (in x-axis), 6 is height (in y-axis) in inches
plt.subplot(1,4,1), plt.imshow(img1, cmap='gray')
plt.subplot(1,4,2), plt.imshow(img2, cmap='gray')
plt.subplot(1,4,3), plt.imshow(img3, cmap='gray')
plt.subplot(1,4,4), plt.imshow(img4, cmap='gray')
plt.show()




# Experiment 1.11: Changing Number of Gray Levels (Downsampling)
"""
What is Gray Level Resolution?
Gray level resolution refers to: The number of intensity levels available for representing a grayscale image.
For an image with b bits per pixel:
L=2^b

where:
L = number of gray levels
b = number of bits per pixel

Example:
If b = 3 bits per pixel, then the number of gray levels is:
L = 2^3 = 8
If b = 4 bits per pixel, then the number of gray levels is:
L = 2^4 = 16
If b = 8 bits per pixel, then the number of gray levels is:
L = 2^8 = 256
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image in grayscale
im = cv2.imread('images/uzair.png', 0)

# Number of bits to test
b = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(b)):
    L = 2 ** b[i]      # Number of gray levels using 2^b formula

    # Quantization
    im1 = np.uint8(np.floor(np.double(im) / L))

    # Normalize for display
    im2 = cv2.normalize(im1, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    plt.subplot(2, 4, i + 1)
    plt.imshow(im2, cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.title('b={}'.format(8 - b[i]))

plt.tight_layout()
plt.show()