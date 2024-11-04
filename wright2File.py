import datetime
import winsound
from time import sleep
import psutil

alarm_fire = datetime.datetime.now()
alarm_cpu_bridge = int(input("Set hour: "))
am_pm = input("am or pm? ")

print(f"Waiting for {am_pm}")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")

    if current_time == f"{alarm_cpu_bridge}:{'00' if alarm_cpu_bridge < 12 else
'12'}":
        print("\nIt's the time!")

        frequency = str(psutil.cpu_freq().current) + " MHz"
        print(f"CPU Frequency: {frequency}")

        with open("copy1.txt", "w") as alarms:
            alarms.write(f'alarm went off at: {am_pm} ({current_time})')
            alarms.close()
    else:
       
        if text:= input('press enter to exit'):
                    input('press enter to exit') == 'enter'
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > alarm_cpu_bridge:
            if cpu_usage > alarm_cpu_bridge:
                bridge = cpu_usage
               
                with open("copy.txt", "w") as alarms: alarms.write(f"\nalarm went off at: {cpu_usage} time ({current_time})")

                alarms.close()
            else:
                print(f'cpu has high strain on it {cpu_usage}')
            winsound.Beep(1000, 1000)
           
        else:
            print(cpu_usage)
        if text == 'enter':
            break
       
        else:
            print(cpu_usage)
