import os

for filename in os.listdir("."):
    pathname = os.path.join(".", filename)
    stat = os.stat(pathname)
    mode = stat.st_mode
    print("stat", stat.filemode(mode))

