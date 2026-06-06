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

import cv2

# Load the image
image = cv2.imread('images/uzair.png')

# Get the original dimensions
original_height, original_width = image.shape[:2]
print("Original dimensions:", (original_height, original_width))

# Define the scaling factor (e.g., 0.5 for halving the size)
scale_factor = 0.5

# Calculate the new dimensions
new_width = int(original_width * scale_factor)
new_height = int(original_height * scale_factor)
new_dimensions = (new_width, new_height)

# Resize usingINTER_AREA for downsampling (better for reducing size)
downsampled_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_AREA)

# Get the new dimensions
downsampled_height, downsampled_width = downsampled_image.shape[:2]
print("Downsampled dimensions:", (downsampled_height, downsampled_width))

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Downsampled Image', downsampled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()