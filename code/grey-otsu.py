import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('img.png',0) 
ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.imshow(imgf,cmap = 'gray')
plt.xticks([]), plt.yticks([])
# plt.show()
plt.savefig('otsu.png',bbox_inches='tight')