import subprocess
import cmd
from colorama import *

class NetshCommands(cmd.Cmd):
    prompt = "\033[4;32m"+"[usr(cmd/netsh)]"+"\033[0;32m > "+"\033[0;37m"

    def do_setscript(self, args):
        pass

netsh_input = NetshCommands()
