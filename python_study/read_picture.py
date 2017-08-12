import numpy as np
from PIL import Image

im1 = Image.open('/home/zjj/桌面/index.jpeg')
arr = np.array(im1)
print(arr.shape)
# im2 = Image.fromarray(arr)
# im2.show(title='haha')
