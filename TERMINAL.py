import os
import subprocess

i = 1


def cmdrun():    
    os.system("color 01")
    while True:  
        rootdir = os.getlogin() + "@terminal:~$ "
        command = input(rootdir)
        os.system(command)
        cmdrun()
    
cmdrun()
