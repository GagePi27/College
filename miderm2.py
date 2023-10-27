#INF360
#Gage Giffin
#Midterm Project
"""
This is a Python program designed as a simple and easy-to-use install assistant for various operating systems.
After installing the operating system of your choice,
     (currently limited to Linux) you can use this program to start up various parts of your OS.
Want to quickly create a Root user or be walked through your SSH setup? Great!
Get your updates done? Absolutely!

In the future I hope to add Windows support and extra functionality.

REQUIREMENTS
- pyfiglet
- 
"""
##############################
# IMPORTS_A
import os
import sys
import time
import pyfiglet

##############################
# OS CHECK

if sys.platform.startswith('win'):
    system = 'Windows'
elif sys.platform.startswith('linux'):
    system = 'Linux'
elif sys.platform.startswith('darwin'):
    system = 'macOS'
else:
    system = 'unknown'

##############################
# ROOT CHECK (REQUIRED FOR VARIOUS ACTIONS)
# Get User ID
username = os.getuid()
print('-----' * 20 + '\nUsername ID:' + str(username) + '\n')
time.sleep(0.75)

# Check if ROOT
if username == 0:
    print('ROOT user active!')

# Request ROOT access
else:
    while True:
        os.system('clear')
        print('''
*WARNING*
This application requires ROOT access...
Please log into ROOT now.
              ''')
        # Does the ROOT password exist?
        print('Is the root password set? (y/n)')
        rootSet = input('> ')
        rootSet = rootSet.upper()
        # ROOT password does NOT exist
        if rootSet == 'NO' or rootSet == 'N':
            print('Please set your ROOT Password now!')
            os.system('passwd root')
            print('After getting ROOT access, enter the following command...')
            print('     python3 ' + __file__)
            os.system('su -')
        # ROOT password exists
        elif rootSet == 'YES' or rootSet == 'Y':
            print('After getting ROOT access, enter the following command...')
            print('     python3 ' + __file__)
            os.system('su -')
        # Bypass
        elif rootSet == 'BYPASS':
            break
        # Non-Valid Answer
        else:
            os.system('clear')
            print('That is not Valid. Try Again.')

##############################
# PIP CHECK
os.system('apt-get install pip -y')

##############################
# REGULAR FUNCTIONS

# Print Title Function
def title():
    os.system('clear')
    print(pyfiglet.figlet_format('TERMINEX\n'))
    print('-----' * 20)

# Slow Print Function
def slowPrint(input):
    for letter in input:
        print(letter, end='')
        time.sleep(.4)
        sys.stdout.flush()
    print()

# Slow Print Function
def fastPrint(input):
    for letter in input:
        print(letter, end='')
        time.sleep(.05)
        sys.stdout.flush()
    print()

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

#Print Fake Load Function
def fakeLoad(title):
    n = 3
    for i in range(n):
        title()
        print()
        fake = '.....'
        for period in fake:
            print(period, end='')
            time.sleep(.3)
            sys.stdout.flush()

##############################
# MENU FUNCTIONS

# Linux Main Menu Function
def menuLinux(title):
    title()
    print('A. Update and Upgrade')
    print('B. ')
    print('C. Users and Groups')
    print('D. ')
    print('Y. Learn the Truth about this Project')
    print('Z. Exit Program')

def aLinux(title):
    title()
    os.system('apt update && upgrade -y')
    time.sleep(2)

def bLinux(title,fakeLoad):
    title()
#    hostname = socket.gethostname()
#    ipAddr = socket.gethostname(hostname)
#    print('Your IP Address is: ' + ipAddr)
    time.sleep(2)
def cLinux(title):
    title()
    print('Here are the users on this machine...\n')
    time.sleep(.5)
    user_data = []
    with open('/etc/passwd', 'r') as passwd_file:
        for line in passwd_file:
            parts = line.strip().split(':')
            if len(parts) >= 3:
                username = parts[0]
                user_data.append(username)
    for user in user_data:
        print(user)
        time.sleep(.1)
    time.sleep(3)

def yLinux(title):
    title()
    print('The truth is... I wanted to build something I would genuinely use')
    time.sleep(1.5)
    print('In the end though, I have coded enough to not need this program again...')
    time.sleep(5)

##############################
# WELCOME

os.system('clear')
time.sleep(0.2)

print(pyfiglet.figlet_format('Welcome!!'))
print('-----' * 20)
time.sleep(1)

fastPrint('''
Welcome to TERMINEX!

This program is your menu to the world of 
    Linux Terminals...
    Commmand Lines...
    Powershell Terminals...
    AND MORE!!!
      ''')

title()
##############################
# OS(LINUX) ACCEPTANCE
if system == 'Linux':
    print('''CONGRATULATIONS!
* Your OS is currently supported by TERMINEX
     Entering TERMINEX...''')

# UNSUPPORTED OS
else:
    print('''
WARNING!
* Your OS is not currently supported by TERMINEX.
          ''')
    if system != 'Windows' and system != 'macOS':
        print('''     
    TERMINEX does not even know what your OS is.....
    That is an accomplishment.......................
              ''')
    else:
        print('''    
    TERMINEX does not currently support ''' + system.upper() + '''.
    Continuing is NOT recommended.
    * Anything beyond this point has NOT been tested.
    * Anything beyond this point is NOT apart of my midterm... Zeller.
              ''')

    # UNSUPPORTED CONTINUANCE
    while True:
        print('Do you wish to continue? (y/N)')
        choice1 = input('> ')
        choice1 = choice1.upper()
        if choice1 == 'Y' or choice1 == 'YES':
            break  # ENTER PROGRAM
        elif choice1 == 'N' or choice1 == 'NO' or choice1 == '':
            print('\nGoodbye!')
            sys.exit()  # EXIT
        else:
            print('That is not a correct answer. Try Again')

##############################
# MAIN MENU

time.sleep(4)
fakeLoad(title)

while True:
    menuLinux(title)
    menuLinuxInput = input('> ')
    menuLinuxInput = menuLinuxInput.upper()
    if menuLinuxInput == 'A':
        aLinux(title)
    elif menuLinuxInput == 'B':
        bLinux(title,fakeLoad)
    elif menuLinuxInput == 'C':
        cLinux(title)
    elif menuLinuxInput == 'D':
        print('NOT READY')
    elif menuLinuxInput == 'Y':
        yLinux(title)
    elif menuLinuxInput == 'Z':
        title()
        print('Thank you. Goodbye!')
        time.sleep(2)
        os.system('clear')
        sys.exit()
    else:
        blinky('That is not valid. Try Again.', title)

