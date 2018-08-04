import os
file_list = os.listdir("C:\Users\shahd\Downloads\BootCamp\python\prank")
print(file_list)
print("current work directory " + os.getcwd()) #is python since file_rename.py is in it
os.chdir("C:\Users\shahd\Downloads\BootCamp\python\prank") #we are now in prank
for file_name in file_list: 
   os.rename(file_name, file_name.translate(None , "0123456789"))
#first parameter of translate function is a table.
#which is translate one set of charachters to anthor set.
#the second represent the char that we want to remove.
print("current work directory " + os.getcwd()) #is python since file_rename.py is in it
os.chdir("C:\Users\shahd\Downloads\BootCamp\python")

