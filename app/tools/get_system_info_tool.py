import platform
import psutil #type:ignore

def get_system_info():
    """
    Returns system information including OS, architecture, CPU, and memory details.
    """
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "CPU": platform.processor(),
        "Total Memory": psutil.virtual_memory().total,
        "Available Memory": psutil.virtual_memory().available,
    }
    return system_info
