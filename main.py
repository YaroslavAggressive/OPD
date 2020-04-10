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
dataStorage = DataSet(Constants.archive_name)
print(dataStorage.get_size())
img, mask = dataStorage.get_image(0)
if mask is None:
    print("NONE")
else:
    print("Success")


batch_size = 5
dataStorageSize = dataStorage.get_size()
# 3400 для теста

# 1 - разделить на тест и трейн (или делать пакетно, т.е. менять трейн после обучения на одном "пакете" данных
index_order = np.random.permutation(dataStorageSize)
train_indexes = index_order[1:dataStorageSize - 3400]
test_indexes = index_order[dataStorageSize - 3400:dataStorageSize]


# 2 - перемешать рандомно тест и трейн (через order как на фото), берем часть и загнать это в словарь {"test": {data...}, "train": {data...}}
# 3 - пропустить через обучение на (1-???) эпохе
# повторить пункт 2 пока не будет достигнута точность или показатели перестанут меняться



