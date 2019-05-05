#from colors import *
import os
import getpass
import time
import argparse

# - Normal colors - #
red = "\033[0;31m"
blue = "\033[0;34m"
green = "\033[0;32m"
yellow = "\033[0;33m"
white = "\033[0;37m"
violet = "\033[0;35m"
cian = "\033[0;36m"



# - This script allows the user to open the NetHack console from their terminal - #
user = getpass.getuser()

try:
    # - if pip exist - #
    import pip._internal as pip

except ImportError:
    pipstats = red + "\033[1mERR"

else:
    pipstats = green + "\033[1mOK"

#print("{}pip\t{}[{}{}]".format(cian, white, pipstats, white))
print("\n" + cian + "\033[1mpip" + white + "................." + white + "[" + pipstats + white + "]")
if pipstats == red + "\033[1mERR":
    print(cyan + "\033[1m[NT] Wait, installing pip . . .")
    os.system("cd config && python get-pip.py")
    print(cyan + "\033[1m[NT] Installed")

else:
    pass

try:
    from colorama import *

except ImportError:
    coloramastats = red + "\033[1mERR"

else:
    coloramastats = green + "\033[1mOK"

time.sleep(1)
print("{}\033[1mcolorama{}............[{}{}]".format(cian, white, coloramastats, white))
if coloramastats == red + "\033[1mERR":
    print(cyan + "\033[1m[NT] Wait, installing colorama  . . .")
    os.system("pip install colorama")
    print(cian + "\033[1m[NT] Testing . . .")
    try:
        from colorama import *
        init()
        print(Fore.GREEN + "[NT] Testing green color")
    except Exception as e:
        print(red + "[NT] Error: {}".format(e))

else:
    pass


try:
    from cryptography.fernet import *

except ImportError:
    cryptostats = red + "\033[1mERR"

else:
    cryptostats = green + "\033[1mOK"

time.sleep(1)
print("{}\033[1mcryptography{}........[{}{}]\n".format(cian, white, cryptostats, white))
if cryptostats == red + "\033[1mERR":
    print(cian + "\033[1m[NT] Wait, installing cryptography  . . .")
    os.system("pip install cryptography")

else:
    pass

print(green + "[NT] Installation complete\n")
run = str(input(cian + "Do you want to run NetHack?[y/n]: "))
if run == 'y':
    os.system("python NetHack.py -a")

elif run == 'n':
    print(green + 'Have a nice day!')
    exit()
else:
    exit()
