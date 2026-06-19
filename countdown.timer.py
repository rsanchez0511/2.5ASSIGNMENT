from datetime import datetime ##dattime module to validate time in HH:MM:SS format
import time ##time module to create a delay and countdown

def timer():
  while True: ##will repeat asking user for timer in HH:MM:SS form until valid input is entered 
     user_timer = input("Please enter the timer in (HH:MM:SS): ")
     try: 
       t = datetime.strptime(user_timer, "%H:%M:%S") ##reads user input and tries to convert into HH:MM:SS form
       break ##break out of loop if successfully validated user input
     except ValueError:
       print("Invalid format. Please use HH:MM:SS") ##display message and repeats loop for user to enter valid input

  total_seconds = t.hour * 3600 + t.minute * 60 + t.second ##converting all the numbers in HH:MM:SS form into seconds so it can count down

  for x in range(total_seconds, 0, -1): ##countdown loop starting from input time converted to seconds down to zero counting down by 1
        seconds = x % 60 
        minutes = int(x / 60) % 60
        hours = int(x / 3600) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}") ##display formatted time in HH:MM:SS form 
        time.sleep(1) 



  print("TIME'S UP!") ## when countdown finishes display TIME'S UP!

timer()
'''This section will not run until user has entered a valid input in HH:MM:SS form 
    This function takes user input time in HH:MM:SS form and counts down by 1 second 
    Preconditions: time input must be in HH:MM:SS
    Parameters: HH represents Hours MM represents Minutes SS represents Seconds
     Return: countdown in HH:MM:SS form going down from user input time to zero by 1  '''
