#INF360 - Programming in Python
#Gage Giffin
#FINAL ASSIGNMENT

"""
This is my final project for Programming in Python.
I call this program... TERMINEX!
    YOUR personal application for setting up YOUR linux Operating System.

REQUIREMENTS
Python3  - 'sudo apt install python3'
Pyfiglet - 'pip install pyfiglet'

ACTIVATION
First... move to the folder where this program was downloaded to.
    Use 'cd *directory*' to move to the folder and 'ls' to see the available folders.
Then 'python3 Final.py' to start the program.

"""

####################
#IMPORTS_A & LOGGING
import logging

logging.basicConfig(filename='terminexLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')


####################
#IMPORTS_B
import os
import sys
import time
logging.debug('Success! - 1st party modules loaded successfully')

try:
    import pyfiglet
    logging.debug('Success! - Pyfiglet module loaded successfully')
except:
    print('''The Pyfiglet module is missing! Please install on your command line using...
            "pip install pyfiglet"''')
    logging.critical('FAILURE - The Pyfiglet module is missing!')
    sys.exit()

logging.debug('Success! - All modules loaded successfully')


####################
#FUNCTION IMPORTS
try:
    from FinalBaseAppFunctions import *
    logging.debug('Success! - BaseAppFunctions.py loaded successfully')
    from FinalLinuxMenuFunctions import *
    logging.debug('Success! - LinuxMenuFunctions.py loaded successfully')
except:
    print('One or more python files are missing!')
    logging.critical('FAILURE - One or more python files are missing!')
    sys.exit()
    

####################
#OS CHECK
osAcceptDeny(osCheck, title, slowPrint, errorPrint)
logging.debug('Success! - osAcceptDeny function completed!')


####################
#LINUX MENU
loadPrint(title)
while True:
    linuxMenu(title)
    print('\nPlease enter a menu letter...')
    menuInput = input('> ')
    menuInput = menuInput.upper()
    if menuInput == 'A':
        linuxA(title)
    elif menuInput == 'B':
        linuxB(title, slowPrint, loadPrint)
    elif menuInput == 'C':
        linuxC(title, slowPrint)
    elif menuInput == 'D':
        AddRemove = linuxD1(title, slowPrint, errorPrint)
        if AddRemove == 'A':
            linuxD2(title, slowPrint, errorPrint)
        elif AddRemove == 'R':
            linuxD3(title, slowPrint, errorPrint)
    elif menuInput == 'E':
        linuxE(title, slowPrint)
    elif menuInput == 'Y':
        linuxY(title)
    elif menuInput == 'Z':
        linuxZ(title, slowPrint)
    else:
        errorPrint(title)
    
