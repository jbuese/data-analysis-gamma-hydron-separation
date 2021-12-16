import numpy as np
from scipy import ndimage, misc
import matplotlib.pyplot as plt
import cv2

def calcSobelImg(val, blur):
  im = np.array(val, copy=True)
  img = cv2.GaussianBlur(im, ksize=(blur, blur), sigmaX=0)
  sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x
  sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y
  result = cv2.addWeighted(cv2.convertScaleAbs(sobelx), 0.5, cv2.convertScaleAbs(sobely), 0.5, 0, img)
  plt.figure(figsize=(20, 10))
  # left side
  plt.subplot(251).title.set_text("normal")
  plt.imshow(im / im.max())
  plt.subplot(252).title.set_text("sobelX")
  plt.imshow(sobelx)
  plt.subplot(253).title.set_text("sobelY")
  plt.imshow(sobely)
  plt.subplot(254).title.set_text("sobelX&Y")
  plt.imshow(result)
  plt.subplot(255).title.set_text("sobelBinarized")
  plt.contour(result, origin='image')
  plt.axis('equal')
  plt.show()
  return result