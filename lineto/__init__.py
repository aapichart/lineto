""" This is the lineto package """
import subprocess as sp
import requests
from lineto.models import create_db, drop_db
from lineto.models import QueryAllUsers, InsertUser


LINE_ACCESS_TOKEN = "w6ilWGXaacIARjhjHpDidVfYWvVKXB0DF5mdmnlM2gW"
URL = "https://notify-api.line.me/api/notify"


def line_text(message):
    """ This func used for sending mesg to LINE-service"""
    headers = {
        'ContentType': "multipart/form-data",
        'Authorization': "Bearer "+LINE_ACCESS_TOKEN
    }
    msg = {
        'message': message
    }
    responsemsg = requests.request(
        "post", verify=True, url=URL, data=msg, headers=headers
    )
    print(responsemsg.text)


def input_int(inputString, default_number, minInt, maxInt):
    """ This function checks whether input value is integer or not 
        default_number should be input as a string"""
    while True:
        userAnswer = input(inputString) or default_number
        try:
            userAnswer = int(userAnswer)
            if (userAnswer >= minInt) and (userAnswer <= maxInt):
                return userAnswer
            else:
                print("input value is out of range")
        except ValueError:
            print("Thai is not a number!")
    # Checking Value whether it is in interval [minInt, maxInt] or not

def showmenu2(): 
    """ This function will show the second menu """
    while True:
        sp.call('clear', shell=True)
        print("  --------------------------- ")
        print("  [1] CreateDB                ")
        print("  [2] DropDB                  ")
        print("  [3] Add new user            ") 
        print("  [4] Delete User             ")
        print("  [5] Show users              ")
        print("  [6] Return to MainMenu      ")
        print(" ---------------------------- ")
        userchoice2 = input_int("Please select your choice [3]: ", "3", 1, 6)
        if userchoice2 == 1:
            create_db()
            input("Press Enter to Continue: ")
        elif userchoice2 == 2:
            drop_db()
            input("Press Enter to Continue: ")
        elif userchoice2 == 3:
            userName = input("Please enter Line Account: ")
            userToken = input("Please input your token: ")
            outmsg = InsertUser(userName, userToken)
            print(outmsg)
            input("Press Enter to Continue: ")
        elif userchoice2 == 4:
            print("Hello Your select choice 4.")
            input("Press Enter to Continue: ")
        elif userchoice2 == 5:
            outmsg = QueryAllUsers()
            print(outmsg)
            input("Press Enter to Continue: ")
        elif userchoice2 == 6:
            return userchoice2


def showmenu1(userchoice):
    while True:
        sp.call('clear', shell=True)
        print("Select the following menu       ")
        print(" [1] - Manage Users DataBase    ")
        print(" [2] - Send Message to All users")
        print(" [3] - Exit Program             ")
        userchoice = input_int(" Your option [2]: ", "2", 1, 3)
        if userchoice == 2:
            userchoice = input(" Enter your message: ")
            line_text(userchoice)
            return "Exit Success"
        elif userchoice == 1:
            showmenu2()
        else:
            return "Exit Program"


def showmenu(userchoice):
        showmenu1(userchoice)
