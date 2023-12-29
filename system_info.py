import platform

def get_system_info():
    system_info = {}

    system_info['System'] = platform.system()
    system_info['Node'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    return system_info