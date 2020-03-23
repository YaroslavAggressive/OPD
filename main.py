#%% Importing the classes(You need to download pillow, matplotlib
import Constants
import matplotlib.pyplot as plt
from Classes import DataSet

#%% Creating the Dataset
tmp = DataSet(Constants.archive_name)
print(tmp.get_size())
img, mask = tmp.get_image(3000)
if mask is None:
    print("NONE")
else:
    print("Success")
    plt.imshow(img)
    plt.show()
    plt.imshow(mask)
    plt.show()



