import numpy as np
from skimage import io

height = 1000
width = 1000
image = np.random.randint(low=0, high=255, size=(height, width))
io.imsave('scripts/heightmap.jpg', image.astype(np.uint8))


