# -*- coding: utf-8 -*-

from os import path, system
import copy
import os
import os.path
import shutil

i = 0
j = 0
c = 0

#Path and Filename with extension should be entered
while j < 10:               #Provides 10 chances to enter the correct path name. Change if required.
    file_path = input('Please enter the file path with extension: ')
    if os.path.isfile(file_path):
        print('Filepath is correct')
        break
    else:
        print('Filepath is incorrect. ')
        j = j + 1

#To get the copy count
def count(c):
    while True:
        if c.isdigit():
            c = int(c)
            print('Copying %s times...' %c)
            return c
            break
        else:
            print('Enter a valid integer!')
            return c
c = input ('Number of copies you need :')

#Split file name and extension
name, ext = os.path.splitext(file_path)
#print (name, ext)

#Copying Loop
for i in range(int(c)):
    shutil.copy2(file_path, name + str(i) + ext)
    if os.path.exists(name + str(i) + ext):
        print ('Copying File %s : Success' %i)
    else:
        print ('Copying File %s : Error' %i)
