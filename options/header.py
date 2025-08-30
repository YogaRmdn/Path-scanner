from options.color import *
import os
import platform

def clean():
    os.system('cls' if platform == 'nt' else 'clear')


def header():
    print(f"""{BOLD_CYAN}
  _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( P | a | t | h ) ( s | c | a | n | n | e | r )
 \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ {RESET}{BOLD_WHITE}
          
            Author  : Bang yog
            Tools   : Path scanner
         https://github.com/YogaRmdn
{RESET}""")