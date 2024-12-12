import monitoring
import alarms
from monitoring import AlarmSystem
def main():
    alarm_system = AlarmSystem()

# Configure alarms

# Display configured alarms

# Start monitoring
    while True:
        print("\nVälj ett alternativ:")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Avsluta")
        
        choice = input("Val: ")
        
        if choice == '1':
            alarm_system.start_monitoring()
        elif choice == '2':
            alarm_system.configure_alarm()
        elif choice == '3':
            alarms.configure_alarm()
        elif choice == '4':
            alarm_system.display_alarms()
        elif choice == '5':
            alarm_system.display_alarms()
        elif choice == '6':
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()