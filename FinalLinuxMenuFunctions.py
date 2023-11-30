#INF360 - Programming in Python
#Gage Giffin
#FINAL ASSIGNMENT

"""
This is a SECONDARY LEVEL python file.
This should NEVER be directly run via the user and instead run in conjuntion by the main program.

This file holds LINUX menu functions.
These are all the functions and programs that should be run inside linux terminals.
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
#LINUX MENU FUNCTIONS

#Linux Menu
def linuxMenu(title):
    title()
    print('''
A. Update & Upgrade
B. Change User Password
C. List System Users
D. Add/Remove Users
E. Enable SSH
...
Y. The Truth
Z. Exit Program
          ''')


#LinuxA Update & Upgrade
def linuxA(title):
    logging.info(' SysInfo. - User Ran Linux Update & Upgrade')
    title()
    os.system('sudo apt update && sudo apt upgrade -y')
    time.sleep(1)
    os.system('clear')
    print('Update & Upgrade Complete!')
    time.sleep(2)

#LinuxB Root Password Set / Reset
def linuxB(title, slowPrint, loadPrint):
    logging.info(' SysInfo. - User Ran Linux Root Password Set / Reset')
    title()
    print('Set/Reset Account Password')
    slowPrint('WARNING!! This will change the password of the selected account!!')
    time.sleep(.5)
    loadPrint(title)
    while True:
        title()
        print('Please enter the selected account... or Z to exit.')
        passwdChange = input('> ')
        if passwdChange == 'Z' or passwdChange == 'z':
            break
        else:
            os.system(f'sudo passwd {passwdChange}')
            time.sleep(1)

#LinuxC List Users
def linuxC(title, slowPrint):
    logging.info(' SysInfo. - User Ran Linux List Users')
    title()
    slowPrint('Here are the users on this machine...\n')
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
    print('\n\nPress ENTER to continue...')
    wait = input('> ')


#LinuxD Add / Remove Users
def linuxD1(title, slowPrint, errorPrint):
    logging.info(' SysInfo. - User Ran Linux Add / Remove Users (Part A)')
    title()
    while True:
        slowPrint('Would you like to Add or Remove a User? (A/r)')
        addRemove = input('> ')
        addRemove = addRemove.upper()
        if addRemove == 'ADD' or addRemove == 'A' or addRemove == '':
            addRemove = 'A'
            return addRemove
            break
        elif addRemove == 'REMOVE' or addRemove == 'R':
            addRemove = 'R'
            return addRemove
            break
        else:
            errorPrint(title)

def linuxD2(title, slowPrint, errorPrint):
    logging.info(' SysInfo. - User Ran Linux Add / Remove Users (Part B)')
    while True:
        title()
        slowPrint('Please enter the name of your new account... Or Z to exit.')
        userAdd = input('> ')
        if userAdd == 'Z' or userAdd == 'z':
            break
        os.system(f'sudo useradd {userAdd}')
        time.sleep(2)
        while True:
            title()
            slowPrint('Would you like to add this new user to the sudo list? (y/N)')
            sudoAdd = input('> ')
            sudoAdd = sudoAdd.upper()
            if sudoAdd == 'Y' or sudoAdd == 'YES':
                os.system(f'sudo usermod -aG sudo {userAdd}')
                print(f'User: {userAdd} User added with sudo privleges')
                time.sleep(2)
                break
            elif sudoAdd == 'N' or sudoAdd == 'NO' or sudoAdd == '':
                title()
                print(f'User: {userAdd} User added without sudo privileges')
                time.sleep(2)
                break
            else:
                errorPrint(title)
            print('Remember to add a password for your new user from our Change Password Function')
        time.sleep(2)
        

def linuxD3(title, slowPrint, errorPrint):
    logging.info(' SysInfo. - User Ran Linux Add / Remove Users (Part C)')
    while True:
        title()
        slowPrint('Please enter the name of the  account you want to delete... Or Z to exit.')
        print('WARNING! This can cause MAJOR damage to the system!!')
        userDel = input('> ')
        if userDel == 'Z' or userDel == 'z':
            break
        while True:
            title()
            slowPrint(f'Are you sure you want to delete the user account: {userDel} (y/N)')
            confirmDel = input('> ')
            confirmDel = confirmDel.upper()
            time.sleep(1)
            if confirmDel == 'Y' or confirmDel == 'YES':
                os.system(f'sudo deluser {userDel}')
                time.sleep(2)
                title()
                slowPrint(f'User account, {userDel} is now deleted.')
                time.sleep(2)
                break
            elif confirmDel == 'N' or confirmDel == 'NO' or confirmDel == '':
                title()
                slowPrint('Canceling user removal...')
                time.sleep(2)
                break
            else:
                errorPrint(title)


#LinuxD SSH Server
def linuxE(title, slowPrint):
    logging.info(' SysInfo. - User Ran Linux SSH Server Setup')
    title()
    slowPrint('Preparing to install OpenSSH Server...')
    time.sleep(.5)
    os.system('sudo apt install openssh-server')
    slowPrint('\n\n\nOpenSSH Server is sucessfully installed!\n\n')
    time.sleep(.5)
    os.system('sudo systemctl enable ssh')
    time.sleep(.5)
    os.system('sudo ufw allow ssh')
    title()
    print('SSH is now available at... *user*@000.000.000.000')
    print('**root over SSH is not automatically enabled')
    print('\n\nPress ENTER to continue...')
    wait = input('> ')

#Linux Y The Truth
def linuxY(title):
    logging.info(' SysInfo. - User Ran Linux The Truth')
    title()
    print('The truth is... I wanted to build something I would genuinely use')
    time.sleep(1.5)
    print('In the end though, I have coded enough to not need this program again...')
    time.sleep(5)


#LinuxZ End Program
def linuxZ(title, slowPrint):
    logging.info(' SysInfo. - User Ran Linux End Program')
    title()
    slowPrint('Thank you! Goodbye!')
    time.sleep(1)
    os.system('clear')
    sys.exit()
              
                  
    
    
