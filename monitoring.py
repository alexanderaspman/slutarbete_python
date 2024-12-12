import psutil
from time import sleep
import threading

import alarms

class  AlarmSystem:
    def __init__(self):
        # Initialize instance variables in the __init__ method
        self.frequency1 = str(psutil.cpu_freq().current) + " MHz"

        self.alarms = []  # A list to store alarms
        self.monitoring_active = False  # A flag to track if monitoring is active

    def configure_alarm(self):
        # Method to configure alarms
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
            
            level = self.get_valid_input("Ställ in nivå för alarm mellan 0-100: ", int, lambda x: 0 <= x <= 100)
            self.alarms.append((alarm_type, level))
            print(f"{alarm_type} satt till {level}%.")

    def display_alarms(self):
        while True:  # infinite loop starts to make the program running until time matches alarm 
            print("#################")
            sleep(10)
            cpu_usage = int(psutil.cpu_percent(interval=1))
    # ringing alarm + execution condition for alarm
            if   self.alarms == "CPU larm":
                        cpu_usage = psutil.cpu_percent(interval=1)

                        print(f"CPU Frequency: {cpu_usage}")

            
                        print(f"ALARM: {self.alarms} har överskridits! (Aktuell CPU: {cpu_usage}%)")
                        break
            print(f"CPU Frequency: {cpu_usage}")

        


     

            sleep(10)
        # Method to display configured alarms
        if not self.alarms:
            print("Inga larm har konfigurerats.")
        else:
            sorted_alarms = sorted(self.alarms, key=lambda x: x[0])
            for alarm in sorted_alarms:
                    frequency = psutil.cpu_percent(interval=1)
                    memory_usage = psutil.virtual_memory().percent
                    disk_usage = psutil.disk_usage('/').percent
            if self.alarms == "CPU larm" and frequency > self.level:
                print(f"ALARM: {self.alarms} % har överskridits! (Aktuell CPU: {frequency}%)")
            elif self.alarms == "Minneslarm" and memory_usage > self.level:
                print(f"ALARM: {self.alarms}% har överskridits! (Aktuell minnesanvändning: {memory_usage}%)")
            elif self.alarms == "Disklarm" and disk_usage > self.level:
                print(f"ALARM: {self.alarms}% har överskridits! (Aktuell diskanvändning: {disk_usage}%)")
            else:
                print(f"{self.alarms}%")
            
            input("Tryck enter för att fortsätta...")
              

    def start_monitoring(self):
        # Method to start monitoring
        self.monitoring_active = True
        print("Övervakning har startats.")
        self.list_active_monitoring()

    def list_active_monitoring(self):
        # Method to list active monitoring
        if not self.monitoring_active:
            print("Ingen övervakning är aktiv.")
        else:
            print("Övervakning är aktiv.")
            input("Tryck enter för att fortsätta...")

    def get_valid_input(self, prompt, input_type, validation_func):
        # Utility method to get valid input
        while True:
            try:
                user_input = input_type(input(prompt))
                if validation_func(user_input):
                    return user_input
                else:
                    print("Ogiltigt värde. Försök igen.")
            except ValueError:
                print("Ogiltigt värde. Försök igen.")