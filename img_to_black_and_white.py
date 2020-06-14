import numpy as np
from PIL import Image

imgPath = str(input("Your path: "))


def bw_convert():
    img = Image.open(imgPath)
    arr = np.asarray(img, dtype='uint8')
    x, y, _ = arr.shape

    k = np.array([[[0.2989, 0.587, 0.114]]])
    arr2 = np.round(np.sum(arr * k, axis=2)).astype(np.uint8).reshape((x, y))

    img2 = Image.fromarray(arr2)
    img2.save('res.jpg')
    img2.show()
bw_convert()