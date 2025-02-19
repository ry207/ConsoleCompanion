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
    with open('programs/productivity/todo/todo.txt') as f:
        for i, line in enumerate(f):
            print(line[3:4])
            if line[0:8] == x.strftime("%x"):
                print(f"{Fore.GREEN}{i+1}: {line}{Style.RESET_ALL}")
                thingstoday += 1
            else:
                print(f"{i+1}: {line}")
    if thingstoday == 0:
        print("You have nothing to do today")
    else:
        print(f"You have {Fore.BLUE}{thingstoday}{Style.RESET_ALL} thing to do today")

# If the current month is greater than the month in the task, delete it from the todo cause its already done

# or if current month but day is less than also delete it