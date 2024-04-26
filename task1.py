1.System Health Monitoring Script:


import psutil

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    if cpu_usage > CPU_THRESHOLD:
        print("CPU usage is high:", cpu_usage)
        # You can send an alert here

    if memory_usage > MEMORY_THRESHOLD:
        print("Memory usage is high:", memory_usage)
        # You can send an alert here

    if disk_usage > DISK_THRESHOLD:
        print("Disk usage is high:", disk_usage)
        # You can send an alert here

    # Check running processes
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            if process_name:
                print("Running process:", process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    check_system_health()



