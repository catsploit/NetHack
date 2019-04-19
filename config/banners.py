from random import randint
from colorama import *
init()

############################
#         Banners          #
#          UTF-8           #
############################

def print_banner():
    banner = randint(0,100)
    #print(banner)
    print("")

    if banner >= 0 and banner < 25:
        print(Fore.LIGHTBLACK_EX+"[NT] [0.0.1] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []\n")
        print(Fore.GREEN+"> hack\t\t\t\t\t\t\t  "+Fore.LIGHTBLACK_EX+"[]")
        print(Fore.LIGHTBLACK_EX+"[*] Downloading website . . .\t[Sesion1]")
        print("     #Installing backdoor\t[Sesion1-TheFatRat]\t  []")
        print("     #Connecting to TheFatRat\t[Sesion1-TheFatRat]")
        print(Fore.LIGHTGREEN_EX+"//Succesfuly \t[Sesion1]\t\t\t\t  "+Fore.LIGHTBLACK_EX+"[]\n"+Fore.GREEN)
        print(Fore.LIGHTBLACK_EX+" [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []\n")

    elif banner >= 25 and banner < 50:
        print(Fore.GREEN)
        print(" /$$   /$$             /$$     /$$   /$$                     /$$")                   
        print("| $$$ | $$            | $$    | $$  | $$                    | $$")                   
        print("| $$$$| $$  /$$$$$$  /$$$$$$  | $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$")             
        print("| $$ $$ $$ /$$__  $$|_  $$_/  | $$$$$$$$ |____  $$ /$$_____/| $$  /$$/")             
        print("| $$  $$$$| $$$$$$$$  | $$    | $$__  $$  /$$$$$$$| $$      | $$$$$$/")              
        print("| $$\  $$$| $$_____/  | $$ /$$| $$  | $$ /$$__  $$| $$      | $$_  $$")              
        print("| $$ \  $$|  $$$$$$$  |  $$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$ v.1.0.0")             
        print("|__/  \__/ \_______/   \___/  |__/  |__/ \_______/ \_______/|__/  \__//$$$$$$")      
        print("                                                                      |______/")
        print(Fore.RESET)

    elif banner >= 50 and banner < 75:
        print(Fore.RED+Style.NORMAL)
        print(r"     ________________________")
        print(r"    |                        |")
        print(r"    |   RipPrivacy           |")
        print(r"    |                        |")
        print(r" ___|	        [NetHack]    |")
        print(r" \ _|                        |")
        print(r"  \\|                        |")
        print(r"   \|________________________|"+Fore.RESET)
        print("")

    elif banner >= 75 and banner <= 100:
        print(Fore.GREEN+Style.NORMAL)
        print(r"            _   _                _    ")
        print(r"           | | | |              | |   ")
        print(r" _ __   ___| |_| |_v1.0__ _  ___| | __")
        print(r"| '_ \ / _ \ __| '_ \ / _` |/ __| |/ /")
        print(r"| | | |  __/ |_| | | | (_| | (__|   < ")
        print(r"|_| |_|\___|\__|_| |_|\__,_|\___|_|\_\."+Fore.RESET)
        print("")
                                      
                                      

    print(Fore.WHITE+"""\
<<--[[ """+Fore.MAGENTA+"""NetHack Alpha 1.0.0"""+Fore.WHITE+""" ]}
    
        __-[0 exploits - 0 addons  - 0 frameworks]-__
        __-[2 develops - 3 modules - 4 banners   ]-__ by Codebreak1\n""")
