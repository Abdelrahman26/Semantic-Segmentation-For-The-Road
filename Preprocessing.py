import numpy as np


def split_image(image):
    img_np = np.array(image)
    cityscape = img_np[:, :256, :]
    label     = img_np[:, 256: ,:]
    return cityscape, label