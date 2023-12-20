import json

# from mylib_json import *

def doj(filename,fn):
    try:
        a = readj(filename)
        a = fn(a)
        writej(filename,a)
    except:
        pass

def writej(filename,data):
    with open(filename, "w") as f:
        a = json.dump(data, f)

def readj(filename):
    a = {}
    try:
        with open(filename, "r") as f:
            a = json.load(f)
    except:
        pass
    return a

    
def printj(filename):
    print(json.dumps(readj(filename),indent=4))