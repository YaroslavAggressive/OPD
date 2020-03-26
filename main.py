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
img, mask = tmp.get_image(1000)
if mask is None:
    print("NONE")
else:
    print("Success")
    #plt.imshow(img)
    #plt.show()
    #plt.imshow(mask)
    #plt.show()

#%% Augmentation using albumentations library
# step 1: load library. In Anaconda Prompt(Anaconda):
# pip install albumentations


augmentation_path = Constants.augmentation_path

# load images and masks
size = int(tmp.get_size())
images = []
masks = []
batch = 100
for i in range(0, size, batch):
    for j in range(batch):
        im, m = tmp.get_image(i + j)
        images.append(im)
        masks.append(m)

    original_height, original_width = images[0].shape[0], images[0].shape[1]
    # rotate and noise with crop
    aug = Compose([
        RandomSizedCrop(p=0.8, min_max_height=(original_height / 2 - 1, original_height), height=original_height - 1,
                        width=original_width - 1),
        OneOf([
            HorizontalFlip(p=0.6),
            VerticalFlip(p=0.6),
            Transpose(p=0.6)
        ], p=1),
        RandomRotate90(p=0.8),
        MultiplicativeNoise(multiplier=[0.5, 1.5], elementwise=True, per_channel=True, p=0.5)
    ])

    for k in range(batch):
        augmented = aug(image=images[k], mask=masks[k])
        Image.fromarray(augmented['image']).save(augmentation_path + "/Images/" + str(int(size / 2) + k + i) + '.jpeg')
        Image.fromarray(augmented['mask']).save(augmentation_path + "/Masks/" + str(int(size / 2) + k + i) + 'PalleteMask.jpeg')
    images.clear()
    masks.clear()
