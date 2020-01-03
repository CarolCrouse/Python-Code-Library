'''
A python script that extracts multiple zip files into their existing folders

Carol Ann Crouse 2019
'''
import os
import arcpy
import zipfile
import fnmatch


rootPath = r"C:\\Working_Files\\PYTHON_TESTING\\unzipping\\"
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root, filename)).extractall(root)
	


