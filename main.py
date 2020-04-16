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
img, mask = tmp.get_image(0)
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
        if im is None or mask is None:
            im, m = tmp.get_image(0)
        images.append(im)
        masks.append(m)
        print(i + j)

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

    # 1 - разделение на тест и трейн (или делать пакетно, т.е. менять трейн после обучения на одном данных)

index_order = np.random.permutation(dataStorageSize)
train_indexes = index_order[1:dataStorageSize - 3400]
test_indexes = index_order[dataStorageSize - 3400: dataStorageSize]

# 2 - перемешивание трейна и теста + дальнейшее обучение сети в несколько эпох

train = {i: i for i in tmp} # filling in dictionary quantity of training images
tmp = DataSet(Constants.archive_name_test)
test = {i: i for i in tmp} # filling in dictionary quantity of testing images

batchSizeTrain = 10
batchSizeTest = 4

for epoch in range(100):
    order = np.random.permutation(int(tmp.get_size())) # for changing order in each epoch
    for startIndex in range(0, int(tmp.get_size())):

        batchIndexesTrain = order[startIndex: startIndex + batchSizeTrain]
        batchIndexesTest = order[startIndex: startIndex + batchSizeTest]
        k = 0
        for i in batchIndexesTrain:
            tempTrain[i] = {k : train[i]}
            k += 1
        k = 0
        for i in batchIndexesTest:
            tempTest[i] = {k : test[i]}
            k += 1
        FCN.train(tempTrain, epoch)
        FCN.test(tempTest, epoch)