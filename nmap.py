import socket
target = input("enter the ip: ")

for port in range(1 , 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"port {port} is open")
    #if result != 0:
     #   print(f"port {port} is closed")

    s.close()