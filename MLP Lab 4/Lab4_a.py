import cv2
from matplotlib import pyplot as plt

orig = cv2.imread(r'image1.jpg')
image = cv2.imread(r'image1.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
rgb = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)

img_blur = cv2.blur(img, (3, 3), 0)

sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  # Combined X and Y Sobel Edge Detection

plt.subplot(221),plt.imshow(rgb),plt.axis('off')
plt.text(960, -200, 'Original', horizontalalignment='center')
plt.subplot(222),plt.imshow(sobelx),plt.axis('off')
plt.text(960, -200, 'Sobel X', horizontalalignment='center')
plt.subplot(223),plt.imshow(sobely),plt.axis('off')
plt.text(960, -200, 'Sobel Y', horizontalalignment='center')
plt.subplot(224),plt.imshow(sobelxy),plt.axis('off')
plt.text(960, -200, 'Sobel XY', horizontalalignment='center')

plt.show()