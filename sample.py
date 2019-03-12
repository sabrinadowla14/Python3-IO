import os
import shutil

f = open("sample.txt", "r+")
line = f.readline()
f1 = open("sample.txt", "w")
f1.write(line)


shutil.copyfileobj(f, f1)