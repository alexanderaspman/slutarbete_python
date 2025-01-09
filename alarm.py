import datetime
# import winsound  exclusively for windows only,
from time import sleep
import psutil
import datetime
# import winsound  exclusively for windows only,
from time import sleep
import psutil

class Alarm:
    def __init__(self, alarm_fire: datetime.datetime, alarm_cpu: int, frequency: str, nowIs=str(datetime.datetime.now().time())):
        self.alarm_fire = alarm_fire
        self.alarm_cpu = alarm_cpu
        self.frequency = frequency
        self.nowIs = nowIs

    def start_alarm(self):
        while True:  # infinite loop starts to make the program running until time matches alarm
            # convert a time in string
            timestring = self.nowIs[:5]
            print("Time is:- " + str(timestring))
            print("#################")
            sleep(10)
            # ringing alarm + execution condition for alarm
            tempdatetimeobj = datetime.datetime.now()
            alarm_cpu = self.alarm_cpu
            if alarm_cpu > 0:
                print("\nIt's the time!")
                print(f"CPU Frequency: {self.frequency}")
                with open("copy1.txt", "w") as alarms:
                    alarms.write(f'alarm went off at: {timestring} in the  ({self.alarm_cpu})')
            else:
                cpu_usage = psutil.cpu_percent(interval=1)
                if cpu_usage > alarm_cpu:
                    print('cpu has high strain on it')
                    # winsound.Beep(1000, 1000)
                    print("SLICE that shit magic :- " + timestring + " " + str(self.alarm_cpu))
                else:
                    print(cpu_usage)
                print("alarm fire at" + str(self.nowIs[:5]))
                print("\nIt's the time!")
                if timestring == '17:26':  # after slicing operation only you can compare time
                    print('Triggered')
                elif timestring == '17:30':
                    print('again triggered')
                else:
                    print('-_-')
                sleep(10)
                with open("copy1.txt", "w") as alarms:
                    alarms.write(f'alarm went off at: {self.nowIs[:5]} and the cpu usage is {cpu_usage} )')
                alarms.close()

# Example usage
alarm = Alarm(datetime.datetime.now(), 50, str(psutil.cpu_freq().current) + " MHz")
alarm.start_alarm()


                
                    
"""
elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
    
    f= open("alarm.txt","w+")

    for i in range(10):
        f.write(f'{alarm_hour}{alarm_minutes}{am_pm} %d\r\n' % (i+1))  
          
        alarm_hour -= 12
"""