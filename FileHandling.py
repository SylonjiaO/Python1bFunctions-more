#File Handling
#How to read files using python
#How to count the number of lines in a file
#How to check the size of the file

import os

try:
    fv1=open("C:\\Sylonjia\\PythonDescription.txt","r")#Opening the file in read mode
    data=fv1.read()
    print("File Content: ")
    print(data)
    fv1.close
    lines=data.split("\n")
    print("Total number of lines :", len(lines))
    print("Byte Size of The File :", os.path.getsize("C:\\Sylonjia\\PythonDescription.txt"))
except FileNotFoundError:
    print("Sorry Wrong Path, Try Again")

except PermissionError:
    print("Sorry...File Permissions Not Found")

except MemoryError:
    print("Sorry Insufficient Memory")

finally:
    print("The End")
