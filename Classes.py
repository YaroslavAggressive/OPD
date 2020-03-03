# Here will be the definition of classes and structures

import os
from PIL import Image
import cv2


# The class which main function is reading files from the directory
class FileArr:
    def __init__(self, folder=None):
        if folder is None:
            return
        if os.path.exists(folder):
            self.__position = 0
            self.__folder = folder
            self.__files_list = os.listdir(self.__folder)
            self.__size = len(self.__files_list)
        else:
            raise SystemExit

    # Returns current position
    def get_pos(self):
        return self.__position

    # Returns one image if the image_amount is not indicated, otherwise returns the list of images. Can be used for
    # 2 different formats.
    def get_image(self, image_amount=1, mode="CV2"):
        if image_amount == 1:
            if mode is "PIL":
                im = Image.open(self.__folder + '/' + self.__files_list[self.__position])
            else:
                im = cv2.imread(self.__folder + '/' + self.__files_list[self.__position], cv2.IMREAD_GRAYSCALE)
            self.__position += 1
            return im
        images = []
        while image_amount > 0 and self.__position < self.__size:
            if mode is "PIL":
                images.append(Image.open(self.__folder + '/' + self.__files_list[self.__position]))
            else:
                images.append(cv2.imread(self.__folder + '/' + self.__files_list[self.__position], cv2.IMREAD_GRAYSCALE))
            self.__position += 1
            image_amount -= 1
        return images

    # Returns amount of files in directory
    def get_size(self):
        return self.__size
