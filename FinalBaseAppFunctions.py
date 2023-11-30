#INF360 - Programming in Python
#Gage Giffin
#FINAL ASSIGNMENT

"""
This is a SECONDARY LEVEL python file.
This should NEVER be directly run via the user and instead run in conjuntion by the main program.

This file holds base application functions like...
    OS Checks
    Title Screen
    Custom Text Printers

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
#TITLE 

#Title Printer
def title():
    os.system('clear')
    print(pyfiglet.figlet_format('TERMINEX'))
    print('-----' * 10)


####################
#BASE SYSTEM PRINT STATEMENTS

#Slow Print Function
def slowPrint(input):
    for letter in input:
        print(letter, end='')
        time.sleep(.02)
        sys.stdout.flush()
    print()


#Error Print Function
def errorPrint(title):
    n = 8
    for i in range(n):
        os.system('clear')
        title()
        if (i % 2) == 0:
            print('That is incorrect! Try Again!!')
            time.sleep(.5)
        else:
            time.sleep(.5)

#Load Print Function
def loadPrint(title):
    n = 3
    for i in range(n):
        title()
        print()
        fake = '.....'
        for period in fake:
            print(period, end='')
            time.sleep(.3)
            sys.stdout.flush()
    print()

####################
#OS SYSTEMS

#Operating System Checker
def osCheck():
    #OS Windows
    if sys.platform.startswith('win'):
        system = 'Windows'
    #OS Linux
    elif sys.platform.startswith('linux'):
        system = 'Linux'
    #OS MacOS
    elif sys.platform.startswith('darwin'):
        system = 'macOS'
    #OS Unknown
    else:
        system = 'unknown'
    logging.info(f' SysInfo. - Detcted OS: {system}')
    return system


#Operating System Acceptance
acceptText = '''
Congratulations! Your OS is compatible with TERMINEX!
    Entering TERMINEX'''

denialText = '''
Unfortunatly, your OS is not supported by TERMINEX.
Would you like to still enter at your own risk? [Y/n]'''

def osAcceptDeny(osCheck, title, slowPrint, errorPrint):
    title()
    #OS Auto Accept - Linux
    if osCheck() == 'Linux':
        slowPrint(acceptText)
        time.sleep(1)
        logging.info(' SysInfo. - osAcceptDeny auto-accepted on OS: Linux')
    #OS Manual Accept - Non-Linux
    else:
        while True:
            slowPrint(denialText)
            override = input('> ')
            override = override.upper()
            #OS Manual Accept Overide
            if override == '' or override == 'Y' or override == 'YES':
                title()
                slowPrint('Entering Terminex...')
                time.sleep(.5)
                logging.info(f' SysInfo. - osAcceptDeny was manually overridden on OS: {osCheck}')
                break
            #OS Manual Accept Denial
            elif override == 'N' or override == 'NO':
                title()
                slowPrint('Goodbye!')
                logging.info(f' SysInfo. - osAcceptDeny was manually closed on OS: {osCheck}')
                sys.exit()
            #OS Manual Accept Error
            else:
                errorPrint(title)

