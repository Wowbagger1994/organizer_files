import os, re, shutil, send2trash 

PATH = 'D:\\Download'

videoRegEx = re.compile('.*.mkv|.*.avi', re.IGNORECASE)
for foldername, subfolders, filenames in os.walk(PATH):
    for filename in filenames:
        if foldername != PATH and videoRegEx.search(filename) != None:
            print(f'Moved file from {foldername}')
            pathFile = (foldername + '\\' + filename)
            shutil.move(pathFile, PATH)
        