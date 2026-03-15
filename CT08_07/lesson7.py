import os
filepath = os.getcwd()
fullpath = os.path.join(filepath, "CT08_07/demofile.txt")
print(os.path.exists(fullpath))