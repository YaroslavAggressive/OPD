# Here will be the definition of classes and structures

import os
from PIL import Image
import cv2
# Class for dataset


class DataSet:
    def __init__(self, folder):
        if not os.path.exists(folder):
            print("ERROR, WRONG PATH")
            raise SystemExit
        self.__folders_list = []
        self.__images_amount = []
        if os.path.exists(folder):
            self.__position = 0
            self.add_folder(folder)
            self.__length = len(self.__folders_list)
            print(len(self.__folders_list))
        else:
            raise SystemExit

    def add_folder(self, folder_name):
        for cur_folder in os.listdir(folder_name):
            new_path = folder_name + '/' + cur_folder
            if cur_folder == 'Masks' and len(os.listdir(folder_name + '/' + cur_folder)) != 0:
                self.__folders_list.append(folder_name)
                sum = 0
                if len(self.__images_amount) is not 0:
                    sum = self.__images_amount[-1]
                self.__images_amount.append(sum + len(os.listdir(folder_name + "/Pictures")))
                return True
            if cur_folder == 'Pictures':
                return False
            self.add_folder(new_path)
        return False

    def get_image(self, idx):
        j = 0
        while idx > self.__images_amount[j]:
            j += 1
        min_idx = 0
        if j is not 0:
            min_idx = self.__images_amount[j - 1]
        images_list = os.listdir(self.__folders_list[j] + "/Pictures")
        image_path = self.__folders_list[j] + '/Pictures/' + images_list[idx - min_idx - 1]
        mask_name = images_list[idx - min_idx - 1].split("Flying")[0]
        for mask in os.listdir(self.__folders_list[j] + "/Masks"):
            if mask_name in mask:
                return cv2.imread(image_path), cv2.imread(self.__folders_list[j] + "/Masks/" + mask)
        return None, None

    def get_size(self):
        return self.__images_amount[-1]
