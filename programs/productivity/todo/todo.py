import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

x = datetime.datetime.now()

def addtodo():
    date = input("Date(MO/DY/YR): ")
    time = input("Time(HR:SC): ")
    task = input("Task: ")
    fulltask = f"{date} at {time}: {task}\n"
    f = open("programs/productivity/todo/todo.txt", "a")
    f.write(fulltask)
    f.close()

def whattodo():
    thingstoday = 0
    with open('programs/productivity/todo/todo.txt', "r+") as f:
        for i, line in enumerate(f):
            year = line[6:8]
            month = line[0:2]
            day = line[3:5]
            if (x.strftime("%m") > month or x.strftime("%y") > year):
                i =- 1
                continue
            if (day < x.strftime("%d") and month <= x.strftime("%m")):
                i -=1
                continue
            if line[0:8] == x.strftime("%x"):
                print(f"{Fore.GREEN}{i+1}: {line}{Style.RESET_ALL}")
                thingstoday += 1
            else:
                print(f"{i+1}: {line}")
    if thingstoday == 0:
        print("You have nothing to do today")
    else:
        print(f"You have {Fore.BLUE}{thingstoday}{Style.RESET_ALL} thing to do today")
