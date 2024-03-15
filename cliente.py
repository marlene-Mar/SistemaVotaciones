import socket
import time

class Cliente():

    #Se define el host y el puerto
    def __init__(self, host, port):
        self.host = host
        self.port = port
        #Variable que almacena el socket, que es TCP
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def conectaServidor(self):
        #Nos conectamos al servidor
        self.cliente_socket.connect((self.host,self.port))

        #Recibe el mensaje de bienvenida
        mensajeBienvenida = self.cliente_socket.recv(1024).decode()
        print(mensajeBienvenida)

        #Solicita el nombre y apellido al cliente
        nombre = input("Ingresa nombre y apellido: ")
        self.cliente_socket.sendall(nombre.encode())
        
        #Espera a recibir respuesta del servidor
        respuesta_servidor= self.cliente_socket.recv(1024).decode()
        print(respuesta_servidor)

        #Recibe la solicitud de opción del servidor y muestra las opciones
        solOpcion =self.cliente_socket.recv(1024).decode()
        print(solOpcion)

        #Solicita al usuario ingresar la opción deseada
        opcion =input("Ingresa la opción deseada: ")
        self.cliente_socket.sendall(opcion.encode())

        #Espera a recibir la confirmación del servidor
        respuesta_servidor = self.cliente_socket.recv(1024).decode()
        print(respuesta_servidor)
                
            
if __name__ == "__main__":
    #Configuración del servidor a conectarse
    host_servidor = "localhost"
    port_servidor = 4000

    #Inicializar y conectar el cliente al servidor
    cliente=Cliente(host_servidor, port_servidor)
    cliente.conectaServidor()
   