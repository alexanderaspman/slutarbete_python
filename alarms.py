import psutil
import utils
alarms = []

def configure_alarm():
    while True:
        print("\nVälj ett alternativ:")
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmeny")
        
        choice = input("Val: ")
        
        if choice == '1':
            alarm_type = "CPU larm"
        elif choice == '2':
            alarm_type = "Minneslarm"
        elif choice == '3':
            alarm_type = "Disklarm"
        elif choice == '4':
            break
        else:
            print("Ogiltigt val. Försök igen.")
            continue
        
        level = utils.get_valid_input("Ställ in nivå för alarm mellan 0-100: ", int, lambda x: 0 <= x <= 100)
        alarms.append((alarm_type, level))
        print(f"{alarm_type} satt till {level}%.")

def display_alarms(self):
    alarm_system = AlarmSystem(self)

    frequency = str(psutil.cpu_percent(interval=1))
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    if not alarms:
        print("Inga larm har konfigurerats.")
    else:
        sorted_alarms = sorted(alarms, key=lambda x: x[0])
        for alarm in sorted_alarms:
            if alarm[0] == "CPU larm" & frequency >  alarm_system.alarms[0][1]: 
                print(f"alarm {alarm[0]} {alarm[1]}%")
            elif alarm[1] == "Minneslarm" & memory_usage >  alarm_system.alarms[1][1]:
                print(f"alarm {alarm[1]} {alarm[1]}%")
            elif alarm [2] == "Diskalarm" & disk_usage >  alarm_system.alarms[2][1]:
                print(f"alarm {alarm[2]} {alarm[1]}%")
            else: print(f"{alarm[0]} {alarm[1]}%")
            
        input("Tryck enter för att fortsätta...")