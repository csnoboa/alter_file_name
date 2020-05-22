import os

files = os.listdir() # read all the file names in the directory

to_be_alter = input("Old:")
new_name = input("New:")

for file in files:
    if to_be_alter in file:
        file_renamed = file.replace(to_be_alter, new_name)
        os.rename(file, file_renamed) # rename the file 
