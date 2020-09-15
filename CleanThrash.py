import os
import shutil
import pathlib

startpath = 't:\\Movies\\'

list = os.listdir(startpath)
itd, ntd, dtd, suf, sud = 0, 0, 0, 0, 0

for i in range(len(list)):
    if os.path.isdir(startpath+list[i]):
        if (list[i] == '.actors'):
            dtd += 1
        else:
            sud += 1
    else:
        sfx = pathlib.Path(list[i]).suffix
        if (sfx == '.jpg'):
            itd += 1
        elif (sfx == '.nfo'):
            ntd += 1
        else:
            suf += 1

print ("Directories to delele: {}\nImages to delete: {}\nNFO to delete: {}\nSurvived files: {}\nSurvived directories: {}".format(dtd, itd, ntd, suf, sud))



