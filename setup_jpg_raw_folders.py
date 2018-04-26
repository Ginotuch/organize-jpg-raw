import os

root = input("Enter root directory: ")

os.mkdir(os.path.join(root, "cr2"))
os.mkdir(os.path.join(root, "cr2", "deleted"))
os.mkdir(os.path.join(root, "jpg"))

for file in os.listdir(root):
    fullpath = os.path.join(root, file)
    if os.path.isfile(fullpath):
        if file.split(".")[1] == "JPG":
            os.rename(fullpath, os.path.join(root, "jpg", file))
        else:
            if file.split(".")[1] == "CR2":
                os.rename(fullpath, os.path.join(root, "cr2", file))
