import os
import sys

size = {}

def project(pth):
    if not os.path.commonprefix(pth):
        return
    with os.scandir(pth) as files:
        for way in files:
            if os.path.isfile(way):
                fl = 10 ** len(str(os.stat(way).st_size))
                size[fl] = size.get(fl, 0) + 1
            elif os.path.isdir(way):
                project(os.path.join(pth, way))


if len(sys.argv) == 2:
    my_project = sys.argv[1]
else:
    my_project = os.getcwd()

project(my_project)
print(size)