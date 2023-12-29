import psutil
import time

def get_additional_info():
    additional_info = {}

    # Uptime
    uptime = psutil.boot_time()
    additional_info['Uptime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(uptime))

    # Current Date and Time
    additional_info['Current Date and Time'] = time.strftime('%Y-%m-%d %H:%M:%S')

    return additional_info