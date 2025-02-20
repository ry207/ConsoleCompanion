import os

def newproj():
    folderName = input("Folder Name: ")
    os.system(f"mkdir {folderName}")
    askFileOrFolder = input("Would you like to make a file or folder in that directory(y/n): ")
    if askFileOrFolder == "y":
        fileOrFolder = input("Will this be a file or a folder(file/folder): ")
        if fileOrFolder == "file":
            fileName = input("File Name: ")
            extension = input("File Type: ")
            os.system(f"touch {folderName}/{fileName}.{extension}")
        elif fileOrFolder == "folder":
            folderName2 = input("Folder Name: ")
            os.system(f"mkdir {folderName}/{folderName2}")
        else:
            print("Not an option")
    elif askFileOrFolder == "n":
        return
    else:
        print("Not an option")
