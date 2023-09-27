"""
Slow down typing speed if possible...

"""
##############################
#IMPORTS_A
import os
import sys
import time

##############################
#IDLE CHECK (SCRIPT IS MEANT TO BE RUN IN A COMMAND LINE STYLE ENVIRONMENT)

#How to check if running in idle?
#
#
#
#

##############################
#ROOT CHECK (REQUIRED FOR VARIOUS ACTIONS)
#Get User ID
username = os.geteuid()
print('Username ID:' + str(username))
print()
time.sleep(0.75)

#Check if ROOT
if username == 0:
    print('ROOT user active!')

#Request ROOT access
else:
    while True:
        os.system('clear')
        print('''*WARNING*
This application requires ROOT access...
Please log into ROOT now.
          ''')
        print('Is the root password set? (y/n)')
        rootSet = input('> ')
        rootSet = rootSet.upper()
        if rootSet == 'NO' or rootSet == 'N':
            print('Please set your ROOT Password now!')
            os.system('passwd root')
            print()
            print('After getting ROOT access, enter the following command...')
            print('     python3 ' + __file__)
            os.system('su -')
        elif rootSet == 'YES' or rootSet == 'Y':
            print('After getting ROOT access, enter the following command...')
            print('     python3 ' + __file__)
            os.system('su -')
        else:
            os.system('clear')
            n = 8
            for i in range(n):
                os.system('clear')
                if (i % 2) == 0:
                    print('That is not Valid. Try Again.')
                    time.sleep(0.5)
                else:
                    print()
                    time.sleep(0.5)

##############################
#PIP CHECK
os.system('apt-get install pip')

##############################
#IMPORTS_B (NOT PRE-INSTALLED)
try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip

try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')
    import pyfiglet

##############################
#FUNCTIONS
#Print Title Function
def title():
    os.system('clear')
    print(pyfiglet.figlet_format('TERMINEX\n'))
    print('-----' * 20)

#Print Blinky Function
def blinky(input, title):
    n = 8
    for i in range(n):
        os.system('clear')
        title()
        if (i % 2) == 0:
            print(input)
            time.sleep(0.5)
        else:
            print()
            time.sleep(0.5)

#Print Linux Menu
def menuLinux():
    print('A. Update and Upgrade')
    print('B. Net-Tools')
    print('C. ')
    print('D. ')
    print('Y. Learn the Truth about this Project')
    print('Z. Exit Program')

#Print Windows Menu
#def menuWindows():
#    print('A. ')
#    print('B. ')
#    print('C. ')
#    print('D. ')

def continuing():
    print()
    input('Press ENTER to return to menu... ')

def netTools(title):
    os.system('clear')
    title()
    print('NET-TOOLS\n')
    print('A. See ALL Information')
    print('B. See Active Interfaces')
    print('C. See Down Interfaces')
    print('Z. Return to Menu!')

##############################
#WELCOME

os.system('clear')
time.sleep(0.2)

print(pyfiglet.figlet_format('Welcome!!'))

time.sleep(1)

print('''
Welcome to TERMINEX!

This program is your menu to the world of 
    Linux Terminals...
    Commmand Lines...
    Powershell Terminals...
    AND MORE!!!
      ''')

##############################
#OS CHECK

if sys.platform.startswith('win'):
    system = 'Windows'
elif sys.platform.startswith('linux'):
    system = 'Linux'
elif sys.platform.startswith('darwin'):
    system = 'macOS'
else:
    system = 'unknown'


print('System OS: ' + system)
print('-----' * 20 + '\n')
time.sleep(2)

#OS(LINUX) ACCEPTANCE
if system == 'Linux':
    print('''CONGRATULATIONS!
* Your OS is currently supported by TERMINEX
     Entering TERMINEX...''')

#UNSUPPORTED OS
else:
    print('''WARNING!
* Your OS is not currently supported by TERMINEX.''')
    if system != 'Windows' and system != 'macOS':
        print('     TERMINEX does not even know what your OS is.....')
        print('     That is an accomplishment.......................')
    else:
        print('     TERMINEX does not currently support ' + system.upper() + '.')
    print('''* Continuing is NOT recommended.
* Anything beyond this point has NOT been tested.
          ''')

#UNSUPPORTED CONTINUANCE
    while True:
        print('Do you wish to continue? (y/N)')
        choice1 = input('> ')
        choice1 = choice1.upper()
        if choice1 == 'Y' or choice1 == 'YES':
            break #ENTER PROGRAM
        elif choice1 == 'N' or choice1 == 'NO' or choice1 == '':
            print('\nGoodbye!')
            sys.exit() #EXIT
        else:
            print('That is not a correct answer. Try Again')

##############################
#MENU START

time.sleep(5)

while True:
    title()
    menuLinux()
    print()
    print('Please enter a letter.')
    menu = input('> ')
    menu = menu.upper()

    if menu == 'A':
        os.system('apt update && upgrade -y')
        time.sleep(2)
    elif menu == 'B':
        os.system('apt-get install net-tools')
        while True:
            netTools(title)
            print()
            print('Please enter a letter.')
            netMenu = input('> ')
            netMenu = netMenu.upper()
            if netMenu == 'A':
                os.system('ifconfig') ####DO I CONTINUE THE NETTOOLS MENU HERE OR SHOULD IT BE PUT INSDIE THE FUNCTION
                continuing()
            if netMenu == 'Z':
                break
    elif menu == 'Y':
        print('''
The truth about this project is that...
  I wanted to make a program I would genuinely use.
But after learning so much code........
  I will probably never need it again.
              ''')
        time.sleep(7)
    elif menu == 'Z':
        print('Thank you for using TERMINEX! Goodbye!')
        time.sleep(1)
        title()
        sys.exit()
    else:
        blinky('That is not Valid. Try Again.', title)
