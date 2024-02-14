import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('image1.jpg')
img = cv.cvtColor(image, cv.COLOR_RGB2BGR)

blur = cv.GaussianBlur (img,(111,111),111)

plt.subplot(121),plt.imshow(img),plt.title('Original'),plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred'),plt.xticks([]), plt.yticks([])

plt.show()