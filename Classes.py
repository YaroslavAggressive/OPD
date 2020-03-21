import os
from PIL import Image


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
        i = 0
        while idx > self.__images_amount[i]:
            i += 1
        min_idx = 0
        if i is not 0:
            min_idx = self.__images_amount[i - 1]
        image_path = self.__folders_list[i] + '/' + os.listdir(self.__folders_list[i])[i - min_idx]

        return Image.open(image_path)
