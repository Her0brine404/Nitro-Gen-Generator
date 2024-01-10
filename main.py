import random
import string
from colorama import Fore, Back, Style
from os import system
import time

system("title Nitro Gen by: github.com/Her0brine404/Nitro-Gen-Generator")

title = ("""
888b    888 d8b 888                          .d8888b.                    
8888b   888 Y8P 888                         d88P  Y88b                   
88888b  888     888                         888    888                   
888Y88b 888 888 888888 888d888 .d88b.       888         .d88b.  88888b.  
888 Y88b888 888 888    888P"  d88""88b      888  88888 d8P  Y8b 888 "88b 
888  Y88888 888 888    888    888  888      888    888 88888888 888  888 
888   Y8888 888 Y88b.  888    Y88..88P      Y88b  d88P Y8b.     888  888 
888    Y888 888  "Y888 888     "Y88P"        "Y8888P88  "Y8888  888  888 
                                                                         
    https://github.com/Her0brine404/Nitro-Gen-Generator                    
""")
print(Fore.BLUE + Style.BRIGHT + title)

def generate_code():
    code = 'https://discord.gift/' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
    return code

def create_codes_file(amount):
    codes = [generate_code() for _ in range(amount)]
    with open('Nitro.txt', 'w') as file:
        file.writelines('\n'.join(codes))

amount = int(input("Input amount: "))

create_codes_file(amount)
an = (f"[+] {amount} Discord gift codes have been generated and saved in Nitro.txt file.")
print(Fore.GREEN + Style.BRIGHT + an)

time.sleep(3)  

print(Fore.RESET + Style.RESET_ALL)
