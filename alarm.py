import datetime
import winsound  # exclusively for windows only,
from time import sleep

# if you are on any other system you can use 'playsound' or 'simpleaudio' module.
alarm_fire = datetime.datetime.now
alarm_hour = int(input("Set hour: "))
alarm_minutes = int(input("Set minutes: "))
am_pm: str = input("am or pm? ")

print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

# time conversion
# because datetime module returns time in military form i.e. 24 hrs format
if am_pm == 'pm':  # to convert pm to military time
    alarm_hour += 12

elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
    alarm_hour -= 12

else:
    pass

while True:  # infinite loop starts to make the program running until time matches alarm time
    print("#################")

    # ringing alarm + execution condition for alarm
    tempdatetimeobj = datetime.datetime.now()

    if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
        now = str(datetime.datetime.now().time()) # convert a time in string

        print("Time is:- " + str(now))

        timestring:str= now[:5] 
     # Slice the time for eg time is 17:02:52:23656 it will 
          
        print("\nIt's the time!")
        winsound.Beep(1000, 1000)
      

      

       

                    
        print("SLICE that shit :- "+ timestring)

        if timestring == '17:26' :  # after slicing operation only you can compare time  

            print('Triggered')

        elif timestring == '17:30' :

            print('again triggered')

        else :
            print('-_-')        

    sleep(60)


