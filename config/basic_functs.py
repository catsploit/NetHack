import os
from colorama import *
from config.banners import *
init()

######################################
#           Basic Functions          #
#                                    #
######################################

def found_file(arch):
    for r, d, f in os.walk('C://'):
        for files in f:
            if files == arch:
                path = os.path.join(r,files)
                print(Fore.GREEN+'//Succesfuly -'+arch+' created in',path+Fore.RESET)

def list_dir():
    print("")
    ls = os.listdir()
    for arch in ls:
        print("-",arch)

    print("")

def help():
    print(Fore.LIGHTBLACK_EX+""">> Help list:
        help           --> Show this list
        cls            --> Clean up the screen
        exit           --> Exit the program
        banner         --> Change banner
        credits        --> Credits: Those who created this project, etc
        import         --> Import a module in the program
        cwd            --> Current working directory
        listdir        --> List directory\n"""+Fore.RESET)

def cleanscreen():
    os.system('cls')

def current_working_directory():
    print(Fore.CYAN+Style.BRIGHT+'Actual directory:\n\t'+os.getcwd()+Fore.RESET)
    print("")

def credits():
    print(Fore.BLACK+Style.BRIGHT+"""\
 [NetHack v1.0.0]
   > Developers:
     *KristianDeveloper
     *Blackout

   > Debugger:
     *KristianDeveloper\n"""+Fore.RESET)

def exit_program():
    print(Fore.CYAN+Style.BRIGHT+"[NT] > //Quiting . . .")
    exit()