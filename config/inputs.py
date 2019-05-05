try:
    from colorama import *
except ImportError:
    print("[NT] No main module 'colorama'")
    exit()
from config.basic_functs import *
from config.banners import *
import cmd
import os
import getpass
import subprocess
init()

#############################
#          Standart         #
#           Input           #
#############################

class BasicCommands(cmd.Cmd):
    prompt = "\033[4;32m"+"[usr]"+"\033[0;32m > "+"\033[0;37m"

    def do_help(self, args):
        help()

    def do_cwd(self,args):
        current_working_directory()

    def do_ls(self, args):
        list_dir()

    def do_cls(self, args):
        cleanscreen()
        print_banner()

    def do_exit(self,args):
        exit_program()

    def do_getwifipass(self, args):
        list=[]
        password_list=[]

        data=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        for i in data:
            if i.startswith("    Perfil de todos los usuarios     : "):
                value=i.replace("    Perfil de todos los usuarios     : ", "")
                if value.endswith("\r"):
                    element=value.replace("\r", "")
                    list.append(element)

        for i in list:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', "name={}".format(i), 'key=clear'])
            resultados=str(results).split("\\n")
            puliendo=resultados[30].replace("    Contenido de la clave  : ", "")
            password=puliendo.replace("\\r", "")
            password_list.append(resultados)

        dicionario={}
        cont=0
        for i in list:
            dicionario[i]=password_list[cont]
            cont+=1

        print(dicionario)

    def do_credits(self, args):
        credits()

    def do_import(self, args):
        user = getpass.getuser()
        modules = os.listdir('C://Users/'+ user +'/NetHack/modules')
        if args in modules:
            if args == 'bluetooth':
                from modules import bluetooth
                print(Fore.CYAN+Style.BRIGHT+"[NT] Imported {}\n".format(args)+Fore.RESET+Style.RESET_ALL)

        else:
            print(Fore.RED+Style.NORMAL+"[NT] Error: '{}' module do not exist\n".format(args))

    def do_banner(self,args):
        os.system('cls')
        print_banner()

    def emptyline(self):
        print('')

    def default(self, args):
        print(Fore.RED+Style.NORMAL+"[NT] Unknown command '{}'\n".format(args))

    def precmd(self, args):
        args.lower()
        return(args)

#Resumir codigo con funcion nueva embarcando el import de modulos
