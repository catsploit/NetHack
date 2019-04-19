from colorama import *
import os
import getpass

# - This script allows the user to open the NetHack console from their terminal - #
user = getpass.getuser()
try:
    # - if pip exist - #
    import pip._internal as pip

except ImportError:
    os.chdir('C://Users/' + user + '/NetHack/config')
    os.system('python get-pip.py')
    os.system('python packages.py')

else:
    from colorama import *
    init()
    print(Fore.GREEN + "[NT] Installation complete\n")
    run = str(input("Do you want to run NetHack?[y/n]: "))
    if run == 'y':
        os.chdir('C://Users/' + user + '/NetHack')
        os.system('python NetHack.py')
    elif run == 'n':
        print('Have a nice day!')
        exit()
    else:
        exit()
