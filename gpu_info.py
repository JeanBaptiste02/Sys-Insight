import psutil

def get_gpu_info():
    gpu_info = {}

    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        for i, gpu in enumerate(gpus):
            gpu_info[f"GPU {i+1} Name"] = gpu.name
            gpu_info[f"GPU {i+1} Memory Total"] = gpu.memoryTotal
            gpu_info[f"GPU {i+1} Memory Free"] = gpu.memoryFree
            gpu_info[f"GPU {i+1} Memory Used"] = gpu.memoryUsed
    except ImportError:
        # GPUtil is not installed
        gpu_info["GPU Information"] = "GPUtil module not found"

    return gpu_info