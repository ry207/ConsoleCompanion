from programs.productivity.todo.todo import addtodo, whattodo
from programs.productivity.newproject import newproj

from programs.system import *
from programs.automation import *
from programs.hacking import *
from programs.executables import *
from programs.misc import *

def title():
    print(r"  _____                      _         _____                                  _             ")
    print(r" / ____|                    | |       / ____|                                (_)            ")
    print(r"| |     ___  _ __  ___  ___ | | ___  | |     ___  _ __ ___  _ __   __ _ _ __  _  ___  _ __  ")
    print(r"| |    / _ \| '_ \/ __|/ _ \| |/ _ \ | |    / _ \| '_ ` _ \| '_ \ / _` | '_ \| |/ _ \| '_ \ ")
    print(r"| |___| (_) | | | \__ \ (_) | |  __/ | |___| (_) | | | | | | |_) | (_| | | | | | (_) | | | |")
    print(r" \_____\___/|_| |_|___/\___/|_|\___|  \_____\___/|_| |_| |_| .__/ \__,_|_| |_|_|\___/|_| |_|")
    print(r"                                                           | |                              ")
    print(r"                                                           |_|                              ")
    print("\n\n\n")

def productivity():
    print("Welcome to the productivity page!\nHere you are able to get some productive things done. To start, select the function you would like to use.")
    print("1. Start a new project")
    print("2. Add to to-do list")
    print("3. View to-do list")
    func = int(input("Enter here: "))
    print("\n\n")
    if(func == 1):
        newproj()
    elif(func == 2):
        addtodo()
    elif(func == 3):
        whattodo()
    else:
        print("That was not an option...")

def system():
    print("Welcome to the system page!\nHere you are able to get system information on your computer. To start, select the type of computer you are on, then the function you would like to use.")
    print("1. Windows")
    print("2. Mac")
    print("3. Ubuntu/Debian Linux")
    print("4. Arch Linux")
    func = int(input("Enter here: "))
    if(func == 1):
        print("Windows")
    elif(func == 2):
        print("Mac")
    elif(func == 3):
        print("Ubuntu/Debian Linux")
    elif(func == 4):
        print("Arch Linux")
    else:
        print("That was not an option...")

def hacking():
    print("Welcome to the hacking page!\nHere you are able to run different hacking scripts or commands. To start, select the function you would like to use.")
    print("1. Nmap")
    print("2. Ssh")
    print("3. OSINT")
    print("4. Wifi Hacking")
    func = int(input("Enter here: "))
    if(func == 1):
        print("Nmap")
    elif(func == 2):
        print("Ssh")
    elif(func == 3):
        print("OSINT")
    elif(func == 4):
        print("Wifi Hacking")
    else:
        print("That was not an option...")

def automation():
    print("Welcome to the automation page!\nHere you are able to run different automation scripts.. To start, select the script you would like to use.")
    print("1. Research")
    print("2. News")
    print("3. Wikipedia")
    print("4. Stocks")
    func = int(input("Enter here: "))
    if(func == 1):
        print("Research")
    elif(func == 2):
        print("News")
    elif(func == 3):
        print("Wikipedia")
    elif(func == 4):
        print("Stocks")
    else:
        print("That was not an option...")

def executables():
    # Have to work on this one some more. this is just a starter
    print("Welcome to the executables page!\nHere you are able to run executables in the \"Executables\" folder. To start, select the Executable you would like to use.")
    exec = ["ytdlp", "putty", "wireshark"]
    for ex in exec:
        index = exec.index(ex)
        print(f"{index + 1}: {ex}")

def misc():
    print("Welcome to the miscellaneous page!\nHere you can run random commands. To start, select the function you would like to run.")
    print("1. Joke")
    print("2. Fact")
    print("3. Motivation")
    func = int(input("Enter here: "))
    if(func == 1):
        print("Joke")
    elif(func == 2):
        print("Fact")
    elif(func == 3):
        print("Motivation")
    else:
        print("That was not an option...")

def main():
    title()
    print("Welcome to the console companion! This application will let you complete many tasks all within the console.\nTo start select the function you would like to perform.\n\n")
    while(True):
        print("\n\n")
        print("1. Productivity")
        print("2. System")
        print("3. Hacking")
        print("4. Automation")
        print("5. Executables")
        print("6. Misc")
        print("7. Exit")
        function = int(input("\n\nEnter class of function here: "))
        print("\n\n")
        if(function == 1):
            print("Productivity")
            productivity()
        elif(function == 2):
            print("System")
            system()
        elif(function == 3):
            print("Hacking")
            hacking()
        elif(function == 4):
            print("Automation")
            automation()
        elif(function == 5):
            print("Executables")
            executables()
        elif(function == 6):
            print("Misc")
            misc()
        elif(function == 7):
            print("Goodbye.")
            exit(88)
        else:
            print("Not an option....")

if __name__=="__main__":
    main()