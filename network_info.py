import psutil

def get_network_info():
    network_info = {}

    interfaces = psutil.net_if_stats()
    for interface, stats in interfaces.items():
        network_info[f"{interface} Status"] = "Up" if stats.isup else "Down"
        network_info[f"{interface} Speed"] = stats.speed

    return network_info