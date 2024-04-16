"""
# Platform module

The platform module provides a way to access information about the underlying platform such as hardware, operating system, and interpreter 
version info. It allows you to retrieve various system-related details, making it useful for writing cross-platform code or for 
understanding the environment your code is running in.

"""

# print(dir(pt))  # Prints the list of attributes and methods available in the platform module
# print(help(pt))  # Prints detailed help information about the platform module

# Example usage:
# import platform
# from platform import *
# from  platform import systems,platform

import platform as pt

def main():
    # Get the operating system name
    os_name = pt.system()
    print(f"Operating System: {os_name}")

    # Get the Python version
    python_version = pt.python_version()
    print(f"Python Version: {python_version}")

    # Get the machine type
    machine_type = pt.machine()
    print(f"Machine Type: {machine_type}")

    # Get the operating system release
    os_release = pt.release()
    print(f"OS Release: {os_release}")

    # Get the platform
    platform_info = pt.platform()
    print(f"Platform: {platform_info}")

    # Get the architecture
    arch_info = pt.architecture()
    print(f"Architecture: {arch_info}")

    # Get the processor name
    processor_name = pt.processor()
    print(f"Processor: {processor_name}")

    # Get the computer's network name
    node_name = pt.node()
    print(f"Node Name: {node_name}")

    # Get detailed system information
    system_info = pt.uname()
    print("System Information:")
    print(f"System/OS: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

if __name__ == "__main__":
    main()
