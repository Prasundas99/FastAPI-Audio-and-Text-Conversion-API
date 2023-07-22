import psutil

def get_ram_available_mb():
    """Gets the RAM available in MB."""

    try:
        ram_available = psutil.virtual_memory().available
        return ram_available / 1048576
    except ImportError:
        return None