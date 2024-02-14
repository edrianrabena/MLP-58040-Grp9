import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('image1.jpg')
img = cv.cvtColor(image, cv.COLOR_RGB2BGR)
median = cv.medianBlur(img,99)

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred'),plt.xticks([]), plt.yticks([])

plt.show()