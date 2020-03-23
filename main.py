#%% Importing the classes(You need to download pillow, matplotlib
import Constants
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from Classes import DataSet
# for augmentation
import numpy as np
from albumentations import (
    PadIfNeeded,
    HorizontalFlip, VerticalFlip, Transpose, RandomRotate90,
    CenterCrop, Crop, RandomSizedCrop,
    Compose, OneOf,
    MultiplicativeNoise
)
#%% Creating the Dataset
tmp = DataSet(Constants.archive_name)
print(tmp.get_size())
img, mask = tmp.get_image(2)
if mask is None:
    print("NONE")
else:
    print("Success")
    plt.imshow(img)
    plt.show()
    plt.imshow(mask)
    plt.show()

#%% Augmentation using albumentations library
# step 1: load library. In Anaconda Prompt(Anaconda):
# pip install albumentations

# load images and masks
size = int(tmp.get_size())
images = []
masks = []
for i in range(int(size/2)):
    im, m = tmp.get_image(i)
    images.append(im)
    masks.append(m)

original_height, original_width = images[0].shape[0], images[0].shape[1]
# rotate and noise with crop
aug = Compose([
    RandomSizedCrop(p=0.8, min_max_height=(original_height / 2, original_height + 1), height=original_height, width=original_width),
    OneOf([
        HorizontalFlip(p=0.6),
        VerticalFlip(p=0.6),
        Transpose(p=0.6)
    ], p=1),
    RandomRotate90(p=0.8),
    MultiplicativeNoise(multiplier=[0.5, 1.5], elementwise=True, per_channel=True, p=0.5)
])

augmentation_path = "C:/Users/userr/Desktop/учеба не нужна/прога/python/OPD data/augmentations/"

for i in range(int(size/2)):
    augmented = aug(image=images[i], mask=masks[i])
    Image.fromarray(augmented['image']).save(augmentation_path + str(size / 2 + i) + '.jpeg')
    Image.fromarray(augmented['mask']).save(augmentation_path + str(size / 2 + i) + 'PalleteMask.jpeg')


