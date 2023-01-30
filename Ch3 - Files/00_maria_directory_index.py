import os
from os import path

path=os.path.abspath(os.getcwd())

#make new directory called "result"
dir=os.mkdir("result")

# make new text file "index"
file = open("result/index.txt","w+")

# list items in current path
src=os.listdir()

# byte count
byte_count=0

#write header of index file
file.write("File Index:\n"+"---------------\n")

# only count files and no directories
for f in src:
    if os.path.isfile(f):
        file_size = os.path.getsize(f)
        byte_count += file_size
        file.write(f+"\n")     # write each file in list

#write footer of index file
file.write("\nBytecount: "+str(byte_count))

file.close()




