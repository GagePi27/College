"""
Slow down typing speed if possible...

"""

##############################
#IMPORTS
import os
import sys

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
#WELCOME

print(pyfiglet.figlet_format('Welcome!!'))
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

#OS(LINUX) ACCEPTANCE
if system == 'Linux':
    print('''CONGRATULATIONS!
* Your OS is currently supported by TERMINEX
* Entering TERMINEX...''')

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

print(pyfiglet.figlet_format('\n\nTERMINEX'))
print('THIS IS WHERE THE MENU GOES') #THIS IS WHERE THE MENU GOES
