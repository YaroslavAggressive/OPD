# Here will be the definition of classes and structures

import os
from PIL import Image

# Class for dataset


class DataSet:
    def __init__(self, folder):
        self.__folders_list = []
        self.__images_amount = []
        if os.path.exists(folder):
            self.__position = 0
            self.add_folder(folder)
            self.__length = len(self.__folders_list)
        else:
            raise SystemExit

    def add_folder(self, folder_name):
        if os.path.isfile(folder_name):
            return True
        print(folder_name)
        for cur_path in os.listdir(folder_name):
            new_path = folder_name + '/' + cur_path
            if self.add_folder(new_path):
                self.__folders_list.append(folder_name)
                sum = 0
                if len(self.__images_amount) is not 0:
                    sum = self.__images_amount[-1]
                self.__images_amount.append(sum + len(os.listdir(folder_name)))
                return False
        return False

    def get_image(self, idx):
        j = 0
        while idx > self.__images_amount[j]:
            j += 1
        min_idx = 0
        if j is not 0:
            min_idx = self.__images_amount[j - 1]
        images_list = os.listdir(self.__folders_list[j])
        image_path = self.__folders_list[j] + '/' + images_list[idx - min_idx]
        while idx - min_idx < len(images_list) and images_list[idx - min_idx].find("PalleteMask") is -1:
            print(images_list[idx - min_idx])
            idx += 1
        if idx - min_idx < len(images_list):
            mask_path = self.__folders_list[j] + '/' + images_list[idx - min_idx]
            return Image.open(image_path), Image.open(mask_path)
        return Image.open(image_path), None

    def get_size(self):
        return self.__images_amount[-1]
