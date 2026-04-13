"""
Name: Muhammad Shahmeer Khan
Title: Command Finder
Date Due: 5 Dec, 2025
Description: A program that lefts user select a file, write, read, append or search or delete names from 
"""

import os

def InputFilename():
    """
    Takes in a filename from the user and returns the filename to be stored in a variable later on

    Arguments: None

    Returns: Filename 
    """
    filename = input("Enter file name: ")
    if filename == "":
        filename = "friends.txt"
    elif not filename.endswith(".txt"):
        filename += ".txt"
    return filename

def ValidVal(num1, num2):
    """
    Dosent let user input any number/option outside the range

    Arguments: 
    Maximum number - that the input can not be greater than 
    Minimum number - that the user can not be enter less than

    Returns: Input value
    """
    value = int(input("Input the number: "))
    if value >= num2 and value <= num1:
        print("Invalid value")
    else:
        return value

def ReadNames(filename): 
    """
    Read all the names from the provided file

    Arguments: 
    Filename - The file you need to read names from
    """ 
    print()             
    file = open(filename, "r")
    read = file.readline()
    while read != "":           
        print(read, end="")
        read = file.readline()
    file.close()
    print()

def WriteNames(filename):  
    """
    Writes names to a selected file

    Arguments: 
    filename - the file you want to write names to
    """
    file = open(filename, "w")
    print("Enter what do you want to write, Type 'STOP' to exit: ")
    while True:
        data = input("> ")
        if data == "STOP":
            break
        file.write(data + "\n")
    file.close()
    print()

def SearchNames(filename):
    """
    Searches for a specific name in the list and tells the user if it is in the file

    Arguments: 
    Filename - the file you want to search through for a specific name
    """
    searchName = input("Enter the name to search for: ")
    found = False

    file = open(filename, "r")

    while True:
        name = file.readline()
        if name == "":
            break
        name = name.strip()
        if name == searchName:
            found = True
            break
    file.close()
    if found:
        print(searchName, "is in the file.")
    else:
        print(searchName, "is NOT in the file.")
    print()

def AddNames(filename):
    """
    Adds/Appends further names to the .txt file without removing the previous ones

    Arguments: 
    Filename - the file you want to add further names to
    """
    file = open(filename, "a")
    print("Add Names, Type 'STOP' to exit: ")
    while True:
        data = input("> ")
        if data == "STOP":
            break
        file.write(data + "\n")
    file.close()


def DeleteName(filename):
    """"
    Delets Names that you want to remove from the file

    Arguments: 
    Filename - the file you want to delete a name from
    """
    found = False

    nameToDelete = input("Enter the name you want to delete: ").strip()
    oldFile = open(filename,"r")
    newFile = "temp.txt"
    new_file = open(newFile, "w")

    while True:
        readName = oldFile.readline()

        if readName.strip() == "":
            break
        
        if readName.strip() == nameToDelete:
            found = True
            continue
    
        new_file.write(readName)

    new_file.close()    
    oldFile.close()

    if found == True: 
        os.remove(filename)
        os.rename("temp.txt",filename)
    elif found == False:
        os.remove("temp.txt")
        print("Name was not present in the file")

    print()
        
filename = InputFilename()
while True:
    print("1. Read the File")
    print("2. Write into the File")
    print("3. Search for a Name")
    print("4. Add Names")
    print("5. Delete Names")
    print("6. Change Filename")
    print("7. Quit")

    choice = ValidVal(1,7)
    if choice == 1:
        ReadNames(filename)
    if choice == 2:
        WriteNames(filename)
    if choice == 3:
        SearchNames(filename)
    if choice == 4:
        AddNames(filename)
    if choice == 5:
        DeleteName(filename)
    if choice == 6:
        filename = InputFilename()
    if choice == 7:
        print()
        print("Goodbye!")
        break
        
