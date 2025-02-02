"""
This program will collect a time value from the user, as well as details about a file update to happen at said time, then makes sure the scheduled action happens when due.
This is just beginning to tap into my full potential as a software developer. While this may look somewhat basic,
it is important to note that this is just scratching the surface of what I am capable of. More advanced and adaptable versions of this and many other kinds of programs can be created using the skills I have.

DISCLAIMER: This program is a DEMO PROGRAM, one I created for the express purpose of giving others a taste of what I am capable of with my computer programming skills.
I do not intend for it to be useful for any real world purpose, and I advise that you don't expect that from it either.

README: For more info about what this program does, and to learn about it's licencing restrictions, please refer to the README.txt file that is packaged with this one

To run this program on your own device, you will need a working instance of a Python interpreter on that device. This is due to the fact that Python is an interpreted language, rather than compiled,
so it normally cannot be ran entirely on it's own, as it is dependant on another program to enterpret it's code and execute it.
"""

from datetime import datetime
import time
import sched

def GetCurrentTime(): # Gets the current time of day as a numeric value that can be used to detect when scheduled actions are due.
    now = datetime.now()
    minutes = int(now.strftime("%M"))
    hours = int(now.strftime("%H"))
    result = minutes + (hours * 60)
    return result
schedule = sched.scheduler(GetCurrentTime) # Create tbe schedule object (needed for automatic performance of actions based on time)

def GetLaterTime(input): # Takes user time input and converts it into a numeric value that can be used for scheduling actions
    MinuteRec = False
    Hours = ""
    Minutes = ""
    for i in range(len(input)):
        if input[i] == ':':
            if i != 0:
                MinuteRec = True
        elif MinuteRec:
            Minutes = Minutes + input[i]
        else:
            Hours = Hours + input[i]

    if MinuteRec == False:
        Result = "INVALID"
    elif len(Minutes) > 2 or len(Hours) > 2:
        Result = "INVALID"
    elif int(Minutes) > 59 or int(Hours) > 23:
        Result = "INVALID"
    else:
        Result = int(Minutes) + (int(Hours) * 60)
    return Result


def FileUpdate(content, file): # Updates a file according to the user's specifications when their scheduled time arrives.
    try:
        with open(file, 'w') as File:
            File.write(content)
            File.close()
    except Exception as ERROR:
        print(f"An error occured during the file updating process. Error Details: {ERROR}")

def WaitForTask(): # Basic function that waits until a scheduled action is due, then runs it.
        schedule.run()

def ScheduleTask(): # Will guide the user through the process of entering all the information needed to schedule a file update, then makes sure it happens when due.
    FileName = input("What file would you like to modify? ")
    FileContent = input("What text would you like to put in this file? ")
    TimeInputNeeded = True
    while TimeInputNeeded:
        UpdateTimeInput = input("What time would you like this task to take place? (use time format HH:MM): ")
        try:
            UpdateTime = int(GetLaterTime(UpdateTimeInput))
            TimeInputNeeded = False
        except:
            print ("Invalid time input. Please try again!")
    schedule.enterabs(UpdateTime, 1, FileUpdate, argument = (FileContent, FileName))
    print("Ok, the file update will take place at your scheduled time.")
    WaitForTask()



print("This program will allow you to choose a text file and some new text to put in it,\n then schedule a time today to make that change. \n This is intended as a demo program and should not be expected to\n have any real world value. Please refer to the READMME.txt file that is packaged with\n this program to learn more about it's purpose and licensing restrictions")
Running = True
while Running:
    ScheduleTask()
    Invalid_Reply = True
    while (Invalid_Reply):
        User_Reply = input("The scheduled action has been completed. You can find your file in this program's directory, unless it failed to write.\nWould you like to repeat this demo? (Yes/No): ")
        if (User_Reply == "Yes" or User_Reply == "yes"):
            Invalid_Reply = False
        elif (User_Reply == "No" or User_Reply == "no"):
            Running = False
            Invalid_Reply = False
        else:
            print("Invalid entry. Please try again.")
