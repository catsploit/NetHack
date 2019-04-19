import os
from config.basicfuncts import *

def cmdtroll():
    file = open('C:/Nicolás/NetHack/trolls/terminaltroll.bat','w')
    file.write(':etiq'+os.linesep)
    file.write('start'+os.linesep)
    file.write('goto etiq')
    file.close()

    found_file('terminaltroll.bat')