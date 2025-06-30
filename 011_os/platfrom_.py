import platform

system = platform.system()

if system == "Linux":
    print("Linux user")
elif system == "Windows":
    print("Windows user")
elif system == "Darwin":
    print("Mac user")
else:
    print("Other User")
