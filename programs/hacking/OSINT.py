import csv

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def runOSINT():
    with open('programs/hacking/OSINTlinks.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            i += 1
            print(f"{Fore.MAGENTA}{i}{Fore.CYAN} - {lines[0]}{Style.RESET_ALL}")
        selection = int(input("Which OSINT link would you like to follow(1-26): "))
        getLink(selection)
        

def getLink(selection):
    with open('programs/hacking/OSINTlinks.csv', mode='r')as file:
        csvFile = csv.reader(file)
        i = 0
        for line in csvFile:
            i += 1
            if i == selection:
                print(f"{Fore.BLUE}{line[1]}{Style.RESET_ALL}")
            else:
                continue
