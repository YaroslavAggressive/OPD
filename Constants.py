# Here will be stored objects which are used during the whole period of program

import enum
from Classes import FileArr

# Insert your way
archive_name = "C:/Users/user/Desktop/ultrasound-nerve-segmentation.zip"


# Enum for Errors
class ERRORS(enum.Enum):
    FILE_IS_NOT_EXIST = 1
    FILE_WRONG_FORMAT = 2


# Data
is_data_loaded = False
test_files = FileArr()
train_files = FileArr()
