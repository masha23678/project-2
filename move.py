import os 
import shutil
path = '/Users/masha678/Desktop/python/Class 99'
print("before moving the file:-")
print(os.listdir(path))
source = "/Users/masha678/Desktop/python/Class 99/test.txt"
destination = "/Users/masha678/Desktop/python/Class 99/newFolder"
dest = shutil.move(source,destination)
print("after moving the file:-")
print(os.listdir(path))
