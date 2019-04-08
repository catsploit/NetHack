try:
    from colorama import *
except ImportError:
    print("\033[1;31m"+"[NT] Error: No main module 'colorama'")
    exit()
from config.banners import print_banner
from config.inputs import *
from config.basic_functs import *
import os
import argparse
init()
cleanscreen()

# - Launch modules - #
parser = argparse.ArgumentParser()
parser.add_argument("-a","--all",help="launch all modules",action='store_true')
parser.add_argument("-l","--launch",help="launch some module")
args = parser.parse_args()

if args.all:
    from modules import *
    print(Fore.CYAN+Style.BRIGHT+"[NT] All the modules have been imported"+Fore.RESET+Style.RESET_ALL)

if args.launch:
    modules = os.listdir('C://Users/Nicolás/NetHack/modules')
    #print(modules)
    if args.launch in modules:
        if args.launch == 'bluetooth':
            from modules.bluetooth import *
            print(Fore.CYAN+Style.BRIGHT+"[NT] Imported {}".format(args.launch)+Fore.RESET+Style.RESET_ALL)
        
    else:
        print(Fore.RED+Style.NORMAL+"[NT] Error: '{}' module do not exist".format(args.launch))

# - Call main functions - #
print_banner()

# - Main input - #
if __name__ =='__main__':
    main_input = BasicCommands()
    main_input.cmdloop()

#Mañana añadir funciones de consola, abrir consola, abrir consola desde la terminal y etc con argparse.
#Abriendo la consola desde la terminal, por default se importan todos los modulos pero quiero que se 
#importen los que el usuario ponga en una variable de paquetes a importar por default.
#Añadir funciones de auto completado en un futuro con cmdloop.
#Trabajar en el modulo encode de forma que el usuario escriba sus exploits.
#Trabajar con PyBluez en el bluetooth
#Exploits locales con funcionde sysinfo