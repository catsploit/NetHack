import os

# - This script allows the user to open the NetHack console from their terminal - #
try:
    # - if pip exist - #
    import pip._internal as pip

except ImportError:
    os.system('cd C://Users/Nicolás/NetHack/config')
    os.system('python get-pip.py')
    os.system('python packages.py')

else:
    from colorama import *
    init()
    print(Fore.GREEN + "[NT] Installation complete\n")
    run = str(input("Do you want to run NetHack?[y/n]: "))
    if run == 'y':
        os.system('cd C://Users/Nicolás/NetHack')
        os.system('python NetHack.py')
    elif run == 'n':
        print('Have a nice day!')
        exit()
    else:
        exit()