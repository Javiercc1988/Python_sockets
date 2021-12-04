import socket

HOST = "localhost"
PORT = 63432

#2 AF_INET indica que es IPV4 / SOCK_STREAM indica que es el protocolo TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # Enlazamos este SOCKET el puerto y servidor
    s.listen()  # Ponemos al servidor a ESCUCHAR

    print("Server info:", socket.gethostname(), "Port: ", PORT)
    print("El servidor está listo. Esperando cliente......")


    conn, addr = s.accept() 

    # AQUI EMPIEZA LA PARTE DEL CLIENTE #
    with conn: 
    # Conn como es un objeto tipo SOCKET lo abrimos igual que arriba e indicamos la address que nos hemos conectado
        
        # Antes de empezar el bucle de conversación vamos a almacenar el nombre del usuario
        # En una variable nombre que pasaremos como parametro del prompt
        nombre = conn.recv(1024)
        print(f"Conectado a: {nombre.decode('utf-8')}")
        saludo = (f"Bienvenido al servidor de chat {nombre.decode('utf-8')}")
        conn.send(saludo.encode("utf-8"))
        
        
        while True: # Iniciamos un bucle para que cada vez que recojamos un paquete lo devolvamos como un servidor que hace (ECOS)
            data = conn.recv(1024)

            if data.decode('utf-8') == 'exit':
                break

            print(f"{nombre.decode('utf-8')} dice: {data.decode('utf-8')}")
            send = input("Mensaje desde el servidor: ")
            conn.send(send.encode('utf-8'))