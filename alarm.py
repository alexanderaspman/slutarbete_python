import datetime
# import winsound  exclusively for windows only,
from time import sleep
import psutil
class Alarm():
    def init(self, alarm_fire:datetime,alarm_cpu:int,frequency:str,nowIs=str(datetime.datetime.now().time())):
        
        self.alarm_fire = alarm_fire
        self.alarm_cpu = alarm_cpu
        self.frequency = frequency
        self.nowIs = nowIs
# if you are on any other system you can use 'aysound' or 'simpleaudio' module.


        alarm_fire = datetime.datetime.now
        
    
#alarm_hour = int(input("Set hour: "))
#alarm_minutes = int(input("Set minutes: "))
def start_alarm(self):
        while True:  # infinite loop starts to make the program running until time matches alarm 
      # convert a time in string
            timestring = nowIs[:5]
            print("Time is:- " + str(timestring))
            print("#################")
            sleep(10)
    # ringing alarm + execution condition for alarm
            tempdatetimeobj = datetime.datetime.now()
            alarm_cpu = self.alarm_cpu
            if alarm_cpu == f"{alarm_cpu}:{'cpu overviewd' if alarm_cpu > 0 else
            'cpu overviewd bridge need to be put in or higher den 0'}":
                print("\nIt's the time!")

            print(f"CPU Frequency: {self.frequency}")

            with open("copy1.txt", "w") as alarms:
                alarms.write(f'alarm went off at: {timestring} in the  ({self.alarm_cpu})')

        else:
                cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > alarm_cpu:
            print('cpu has high strain on it')
          #   winsound.Beep(1000, 1000)
            print("SLICE that shit magic :- "+ timestring + " " + self.alarm_cpu)
       
        else:
            print(cpu_usage)
   
        print("alarm fire at"+ str(nowIs[:5]))
        
     # Slice the time for eg time is 17:02:52:23656 it will  
        print("\nIt's the time!")
        
       
        
        

        if timestring == '17:26' :  # after slicing operation only you can compare time  

            print('Triggered')

        elif timestring == '17:30' :

            print('again triggered')

        else :
            print('-_-')        

        

        sleep(10)

       
        
        
        
           
        with open("copy1.txt", "w") as alarms:
                alarms.write(f'alarm whent of at: {nowIs[:5]} and the cpu usage is {cpu_usage} )')
    

                alarms.close()
                alarms.c()  
            alarm_cpu = int(input("Set cpu alarm: "))

         frequency = str(psutil.cpu_freq().current) + " MHz"
         print(f"CPU Frequency: {frequency}")

         print(f"Waiting for cpu wall bridge: {alarm_cpu}")




        start_alarm(fire_alarm=datetime)


                
                    
"""
elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
    
    f= open("alarm.txt","w+")

    for i in range(10):
        f.write(f'{alarm_hour}{alarm_minutes}{am_pm} %d\r\n' % (i+1))  
          
        alarm_hour -= 12
"""