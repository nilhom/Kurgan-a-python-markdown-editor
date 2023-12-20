import os

def getFilesFromPath(path): # Just Files
    try:
        return [files for root, dirs, files in os.walk(path)][0]
    except:
        return []

def getFoldersFromPath(path): # Just Folders
    try:
        return [dirs for root, dirs, files in os.walk(path)][0]
    except:
        return []

def getContentsFromPath(path): # Lists Files and Folders
    try:
        return os.listdir(path) 
    except:
        return []


def writeToFile(name,text):
    try:
        with open(name,"w") as f: 
            f.write(text)
    except:
        pass

def getTextFromFile(name):
    try:
        with open(name,"r") as f:
            ret = f.read()
        return ret
    except:
        pass

def createFile(path):
    try:
        with open(path,"a+") as f: # Creates new file
            ret = f.read()
    except:
        pass

def createFolder(path):
    try:
        os.makedirs(path, mode = 0o777, exist_ok = False)
    except:
        pass