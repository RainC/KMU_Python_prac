import os


#print files list
#path = "/Users/RainC/Library"
#dirfiles = os.listdir(path)
#print(dirfiles)


path = "/"
dirfiles = os.listdir(path)

dir_names = []
file_names = []


for each in dirfiles:
    fullpath = path + each
    if os.path.isdir(fullpath):
        dir_names.append(fullpath+"/")
    else:
        file_names.append(fullpath)


print(file_names)
