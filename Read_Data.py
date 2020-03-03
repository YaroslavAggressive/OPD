import zipfile
import Constants
import os.path
import os
from Classes import FileArr

from Constants import archive_name
from Constants import ERRORS


# Extracting zip archive
def extracting():
	if os.path.exists('DataSet') is False: # If already exists, doesn't anything
		if os.path.exists(archive_name) is False:
			raise SystemExit(ERRORS.FILE_IS_NOT_EXIST)
		if zipfile.is_zipfile(archive_name):
			archive = zipfile.ZipFile(archive_name, 'r')
			archive.extractall('DataSet')
		else:
			raise SystemExit(ERRORS.FILE_WRONG_FORMAT)


#  Function loads train and test directories
def load_data():
	extracting()
	if Constants.is_data_loaded is False:
		Constants.test_files = FileArr('DataSet/test')
		Constants.train_files = FileArr('DataSet/train')
		Constants.is_data_loaded = True
