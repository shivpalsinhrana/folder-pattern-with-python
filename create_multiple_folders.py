import os
from tkinter import *
from tkinter import filedialog


while True:
    
    a = Tk()
    a.file1 = str(filedialog.askdirectory())

    os.chdir(a.file1)
    y = str(input('First part of the folder? '))
    z = int(input('Folder sequence starts from? '))
    x = int(input('Folder sequence ends at? '))

    if x < z:
        print('End value must be greater than or equal to start value')

    elif x == z:
        for i in range(z, (x+1)):
            os.mkdir(y + '_' + str(i))
            print("One Folder Sucessfully Created")
    else:
        for i in range(z, (x+1)):
            os.mkdir(y + '_' + str(i))
        print("Folders Sucessfully Created")

    q = str(input('Do you wish to continue? (y or n)'))

    if q == 'n':
        break
    elif q != 'n' and q != 'y':
        print('Enter only y or n')
        break
    elif q == 'y':
        continue

        
    #Copyright
    #Copyright © Shivpalsinh Rana
