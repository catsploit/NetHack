from netshpy import *
from colorama import *
import cmd

# - Style - #
subline = "\033[4m"
normal = "\033[0m"

class Cmdinput(cmd.Cmd):
    prompt = "{}[{}usr(cmd/){}{}] > {}".format(Fore.GREEN, subline, normal, Fore.GREEN, Fore.WHITE)

    def do_netsh(self, args):
        netsh_input.cmdloop()

    def do_exit(self, args):
        exit()

    def default(self, args):
        print(Fore.RED+Style.NORMAL+"[NT] Unknown command '{}'\n".format(args))

cmd_input = Cmdinput()
cmd_input.cmdloop()
