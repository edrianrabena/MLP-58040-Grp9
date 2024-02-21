import cv2
from matplotlib import pyplot as plt

orig = cv2.imread(r'image1.jpg')
image = cv2.imread(r'image1.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
rgb = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)

img_blur = cv2.blur(img, (3, 3), 0)

edges = cv2.Canny(img_blur,100,200)

plt.subplot(121),plt.imshow(rgb),plt.axis('off')
plt.text(960, -200, 'Original', horizontalalignment='center')
plt.subplot(122),plt.imshow(edges),plt.axis('off')
plt.text(960, -200, 'Sobel X', horizontalalignment='center')

plt.show()