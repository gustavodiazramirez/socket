import socket

# Línea para crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Línea para conectar al servidor
host = '0.0.0.0'  # Escuchar en todas las interfaces
port = 12000  # El puerto en el que el servidor está escuchando
client_socket.connect((host, port))

# Enviar datos al servidor
message = "Hola desde el cliente"
client_socket.send(message.encode('utf-8'))

# Línea para recibir datos del servidor
data = client_socket.recv(1024)  # Aquí se reciben datos del servidor hasta 1024 bytes
print(f"Recibido del servidor: {data.decode('utf-8')}")

# Línea para cerrar el socket del cliente
client_socket.close()
