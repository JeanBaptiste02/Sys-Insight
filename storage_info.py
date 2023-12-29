import psutil

    
def get_storage_info():
    storage_info = {}

    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        storage_info[f"{partition.device} Total"] = partition_info.total
        storage_info[f"{partition.device} Free"] = partition_info.free

    return storage_info