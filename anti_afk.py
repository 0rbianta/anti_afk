import os
import time
import keyboard
from random import randint
from pynput.mouse import Button, Controller


def main():
    check_root()
    print("Welcome to anti-afk cheat for games. Have fun. You can stop script anytime by pressing \"q\".")
    print("I'm understand that I can stop script by pressing \"q\".")
    usr=str(input("USER(yes/no)>> "))
    if(usr=="yes" or usr=="y"):
        antiafk()
    elif(usr=="no" or usr=="n"):
        print("Exiting...")
        exit()
    else:
        print("Please write \"yes\" or \"no\" to continue. Exiting...")
        exit()


def check_root():
    user_profile=os.popen("whoami").read()
    if("root" in user_profile):
        os.system("clear")
    else:
        print("Please run as root.")
        exit()

def antiafk():
    Mouse = Controller()
    while keyboard.is_pressed("q")==0:
        x=randint(0,1000)
        y=randint(0,1000)
        time.sleep(0.5)
        print("Mouse moved to x:",x,", y:",y,sep="")
        Mouse.position = (x, y)
    print("\"q\" pressed. Exitting...")

main()