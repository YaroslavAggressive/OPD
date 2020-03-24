#%% Importing the classes(You need to download pillow, matplotlib)conda install -c anaconda pillow
import Constants
import matplotlib.pyplot as plt
from Classes import DataSet

def GET_SOME_IMAGES(data, a, b):
    for i in range(b-a):
        data.get_image(i)

#%% Creating the Dataset
tmp = DataSet(Constants.archive_name)
print(tmp.get_size())
img, mask = tmp.get_image(100000)
if mask is None:
    print("NONE")
else:
    print("Success")
    #plt.imshow(img)
    #plt.show()
    #plt.imshow(mask)
    #plt.show()

GET_SOME_IMAGES(tmp, 1, 300)



