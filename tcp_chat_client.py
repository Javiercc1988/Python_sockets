import socket

#1 SOCKET DEL CLIENTE
HOST = "localhost"
#127.0.0.1
PORT = 63432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    try:
        c.connect((HOST,PORT))
        print("Conexión extablecida. Bienvenido al servidor :-)")
    except Exception as e:
        print("Error al conectar al servidor: ", e)

# Una vez establecemos la conexión con el servidor vamos a enviar el nombre de usuario
# para que el servidor lo recoja y lo use en su prompt
    nombre = input("Introduce tu nombre de usuario: ")
    c.send(nombre.encode("utf-8"))
    respuesta = c.recv(1024)
    print(f"El servidor dice: {respuesta.decode('utf-8')}")

    while True:

        msg = input("Escribe un mensaje: ")
        c.send(msg.encode("utf-8"))
        respuesta = c.recv(1024)
        if msg == 'exit':
            break
        print(f"El servidor dice: {respuesta.decode('utf-8')}")

print("ADIOS")
