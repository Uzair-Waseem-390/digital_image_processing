# normal
# import cv2

# img = cv2.imread('images/uzair.png')

# cv2.imshow('window_name', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# for gray scale
# import cv2
# img_gray = cv2.imread('images/uzair.png', 0)   # 0 for gray scale, 1 for color, -1 for unchanged
# cv2.imshow('gray_scale', img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Read with OpenCV, Display with Matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/uzair.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # CONVERSION is KEY!
plt.imshow(img_rgb)
plt.show()