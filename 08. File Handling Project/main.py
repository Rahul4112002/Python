from pathlib import Path 
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i+1} : {items}')
        
def createfile():
    readfileandfolder()
    name = input("Please tell your file name:- ")
    p = Path(name)
    try:
        if not p.exists():
            with open(p,'w') as fs:
                data = input("What you want to write in this file:- ")
                fs.write(data)
            print("FILE CREATE SUCCESSFULLY")
        else:
            print("File is already exist")
    except Exception as err:
        print("An Error Occured as {err}")
        
        
def readfile():
    readfileandfolder()
    name = input("Please tell your file name:- ")
    p = Path(name)
    try:
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCCESSFULLY")
        else:
            print("File Does not exists")
    except Exception as err:
        print("An error occurred as {err}")
        

def updatefile():
    readfileandfolder()
    name = input("Tell which file you want to update:- ")
    p = Path(name)
    try:
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of file")
            print("Press 2 for overwriting the data of file")
            print("Press 3 for appending some content in your file")
            
            res = int(input("Tell your response:- "))
            if res == 1:
                name2 = input("Tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                    with open(p, 'w') as fs:
                        data = input("Tell what you want to write this is overwrite the data :- ")
                        fs.write(data)
            
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Tell what you want to append: ")
                    fs.write(" ",data)
    except Exception as err:
        print("An error is occured as {err}")
        

def deletefile():
    try:

        readfileandfolder()
        name = input("whuich file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")
        

print("Press 1 for creating the file")
print("Press 2 for reading the file")
print("Press 3 for updating the file")
print("Press 4 for deletion the file")

check = int(input("Please tell your response:- "))

if check == 1:
    createfile()
    
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()