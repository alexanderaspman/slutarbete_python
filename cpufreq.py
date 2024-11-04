import psutil
import platform
import subprocess
import time
# Get the CPU architecture and frequency information
frequency = str(psutil.cpu_freq().current) + " MHz"
num_cores = psutil.cpu_count(logical=False)
total_logical_cores = psutil.cpu_count(logical=True)

print(f"CPU Frequency: {frequency}")
print(f"Number of Cores (Physical): {num_cores}")
print(f"Total Logical Cores: {total_logical_cores}")

# Get the system's architecture and Python version information
system_arch = platform.machine()
python_version = platform.python_version()

print(f"System Architecture: {system_arch}")
print(f"Python Version: {python_version}")

# Run a command to get the CPU temperature (if supported)
try:
    output = subprocess.check_output(["cat",
"/sys/class/thermal/thermal_zone0/temp"])
    cpu_temp = int(output.decode("utf-8")) / 1000
    print(f"CPU Temperature: {cpu_temp}°C")
except FileNotFoundError:
    print("CPU temperature unavailable on this system.")

# Get the CPU usage statistics
print("\nCPU Usage:")
for i in range(psutil.cpu_count(logical=True)):
    print(f"Core {i}: {(psutil.cpu_percent(percpu=True)[i])}%")
    
    cpu_threshold = 90

try:
    while True:
        # Get the CPU frequency and number of cores
        frequency = str(psutil.cpu_freq().current) + " MHz"
        num_cores = psutil.cpu_count(logical=False)
        total_logical_cores = psutil.cpu_count(logical=True)

        print(f"CPU Frequency: {frequency}")
        print(f"Number of Cores (Physical): {num_cores}")
        print(f"Total Logical Cores: {total_logical_cores}")

        # Get the CPU usage statistics
        cpu_usage = psutil.cpu_percent(percpu=True, interval=1)
        for i, percentage in enumerate(cpu_usage):
            if percentage > cpu_threshold:
                print(f"\nCPU Usage on Core {i} has exceeded the threshold of {cpu_threshold}%")
                break
        time.sleep(1)

except KeyboardInterrupt:
    print("\nScript interrupted by user. Goodbye!")