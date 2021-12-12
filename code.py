import os 
import shutil 
path = '/Users/masha678/Desktop/python/Class 99'
print("before copying file:-")
print (os.listdir(path))
source = "/Users/masha678/Desktop/python/Class 99/test.txt"
destination = '/Users/masha678/Desktop/python/Class 99/test2.txt'
dest = shutil.copy(source,destination)
print("after copying the file:-")
print(os.listdir(path))

