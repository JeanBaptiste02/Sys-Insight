import psutil

def get_cpu_info():
    cpu_info = {}

    cpu_info['CPU Cores'] = psutil.cpu_count(logical=False)
    cpu_info['Logical CPUs'] = psutil.cpu_count(logical=True)
    cpu_info['CPU Usage'] = psutil.cpu_percent(interval=1)

    return cpu_info