import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage.segmentation import watershed
from skimage.feature import peak_local_max

from skimage.measure import regionprops, label

def separate(image):
  # Now we want to separate the two objects in image
  # Generate the markers as local maxima of the distance to the background
  distance = ndi.distance_transform_edt(image)
  print(distance) 

  local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                              labels=image)
  markers = ndi.label(local_maxi)[0]
  labels = watershed(-distance, markers, mask=image)

  fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
  ax = axes.ravel()

  ax[0].imshow(image, cmap=plt.cm.gray)
  ax[0].set_title('Overlapping objects')
  ax[1].imshow(-distance, cmap=plt.cm.gray)
  ax[1].set_title('Distances')
  ax[2].imshow(labels, cmap=plt.cm.nipy_spectral)
  ax[2].set_title('Separated objects')

  for a in ax:
      a.set_axis_off()

  fig.tight_layout()
  plt.show()

  regions = regionprops(labels)
  regions = [r for r in regions if r.area>5]
  print("Number of seperated objects with area >5: ", len(regions)-1)
