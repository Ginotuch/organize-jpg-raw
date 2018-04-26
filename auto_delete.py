import os
from time import sleep

root = input("Enter root directory: ")

while 1:
    jpglist = [x.split(".")[0] for x in os.listdir(os.path.join(root, "jpg"))]
    cr2list = [x.split(".")[0] for x in os.listdir(os.path.join(root, "cr2")) if x != "deleted"]
    for raw in [x + ".CR2" for x in cr2list]:
        if raw.split(".")[0] not in jpglist and raw != "deleted":
            os.rename(os.path.join(root, "cr2", raw), os.path.join(root, "cr2", "deleted", raw))
            print("deleted", raw)

    for undeleted in jpglist:
        if undeleted.split(".")[0] not in cr2list:
            src = os.path.join(root, "cr2", "deleted", undeleted.split(".")[0] + ".CR2")
            dst = os.path.join(root, "cr2", undeleted.split(".")[0] + ".CR2")
            os.rename(src, dst)
            print("undeleted", undeleted)
    sleep(1)
