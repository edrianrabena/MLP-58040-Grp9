import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('image1.jpg')
img = cv.cvtColor(image, cv.COLOR_RGB2BGR)

blur = cv.blur(img,(80,80))
gau = cv.GaussianBlur (img,(111,111),111)
me = cv.medianBlur(img,99)
bi = cv.bilateralFilter(img, 100,200,200)

plt.subplot(331),plt.imshow(blur),plt.xticks([]),plt.yticks([])
plt.text(960, 200, 'Blurred', color='aqua', horizontalalignment='center')
plt.subplot(333),plt.imshow(gau),plt.xticks([]),plt.yticks([])
plt.text(960, 200, 'Gaussian Blur', color='aqua', horizontalalignment='center')
plt.subplot(335),plt.imshow(img),plt.xticks([]),plt.yticks([])
plt.text(960, 200, 'Original', color='aqua', horizontalalignment='center')
plt.subplot(337),plt.imshow(me),plt.xticks([]),plt.yticks([])
plt.text(960, 200, 'Median Blur', color='aqua', horizontalalignment='center')
plt.subplot(339),plt.imshow(bi),plt.xticks([]),plt.yticks([])
plt.text(960, 200, 'Bilateral Filter', color='aqua', horizontalalignment='center')

plt.show()