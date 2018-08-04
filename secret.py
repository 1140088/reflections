import os
file_list = os.listdir("C:\Users\shahd\Downloads\BootCamp\python\")
print("current work directory " + os.getcwd()) 
os.chdir("C:\Users\shahd\Downloads\BootCamp\python\")
for file_name in file_list: 
   os.rename(file_name, file_name.translate(None , "0123456789"))
os.chdir("C:\Users\shahd\Downloads\BootCamp\python")
