# The code is written for dataset from https://www.kaggle.com/c/ultrasound-nerve-segmentation/data
# For other dataset their might be some differences

import Read_Data
import Constants
import matplotlib.pyplot as plt
from Classes import FileArr

Read_Data.load_data()
print(Constants.test_files.get_size())  # if 5508, maybe, everything is nice
image = Constants.test_files.get_image()
plt.imshow(image)
print(image.shape)
