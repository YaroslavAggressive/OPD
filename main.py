#%% Importing the classes(You need to download pillow, matplotlib
import Constants
import matplotlib.pyplot as plt
from Classes import DataSet

#%% Creating the Dataset
tmp = DataSet(Constants.archive_name)
print(tmp.get_size())
#img = tmp.get_image(10000)
print("Success")
plt.imshow(img)
plt.show()



