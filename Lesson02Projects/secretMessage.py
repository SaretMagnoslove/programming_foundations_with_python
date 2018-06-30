import os

def renameFiles():
    
    # get file names from folder
    fileList = os.listdir(r"E:\Courses\udacity\FoundationTemp\Lesson01Projects\prank")
    print(fileList)
    savedPath = os.getcwd()
    # for each file: rename file name
    os.chdir(r"E:\Courses\udacity\FoundationTemp\Lesson01Projects\prank")
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file in fileList:
        os.rename(file, file.translate(table))
    os.chdir(savedPath)         
renameFiles()
