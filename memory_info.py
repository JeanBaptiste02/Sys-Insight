import psutil

def get_memory_info():
    memory_info = {}

    virtual_memory = psutil.virtual_memory()
    memory_info['Total RAM'] = virtual_memory.total
    memory_info['Available RAM'] = virtual_memory.available
    memory_info['Used RAM'] = virtual_memory.used
    memory_info['RAM Usage Percentage'] = virtual_memory.percent

    return memory_info