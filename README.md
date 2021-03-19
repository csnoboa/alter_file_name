# alter_file_name

0:      Install python 3.7: 
        https://www.python.org/ftp/python/3.7.7/python-3.7.7.exe

1: 
        Put the "main.py" and "alter_names.bat" in somewhere you will not delete ( Ex: C:\scr\alter_names\ )

        If you put in other directory, change the path in the alter_names.bat

2: 
        Now, open the regedit (Type Win+R, then type regedit or search for regedit in the windows search to open the Registry Editor)

3:
        create a key in: Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\

4:
        named Alter Files Name

5:
        And create a key named command

6:
        edit the command key to:  C:\scr\alter_names\alter_names.bat 
        (or the path you put the alter_names.bat)
        
        
Demonstration:
![](clip0014.gif)
