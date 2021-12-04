import socket

# CLASE DEL DIA 23/9/2021


#1 SOCKET DEL CLIENTE
HOST = "192.168.0.16"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    for puerto in range (80,1580):
        try:
            c.connect((HOST,puerto))
            print(f"El puerto {puerto} está abierto")
        except Exception as e:
            print(f"El puerto {puerto} está cerrado")
