import os
import shutil

Source = input("Enter Source Folder Name")
destination = input("Enter destination folder name")
listofFiles = os.listdir(Source)
for file in listofFiles:
    shutil.copy((Source+file),destination)