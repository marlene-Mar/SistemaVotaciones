import socket
import threading
import time

class Servidor:
    # Arreglo de clientes
    nombresClientes = ["Rodrigo López", "María García","Sofia Flores",
                    "Leonardo Reyes", "Mateo Cruz", "Diego Díaz",
                    "Julieta Torres", "Monica Ortega", "Tania Salazar", 
                    "Micaela Alcaide","Baltasar Montes", "Mariano Izquierdo"]

    # Proceso para manejar la conexión con cada cliente
    def manejarCliente(self, cliente_socket, direccion):
        try:
            cliente_socket.sendall("Bienvenido al sistema de votaciones.\n".encode())
            
            #Se almacena el nombre ingresado por el cliente
            nombreCliente = cliente_socket.recv(1024).decode().strip()
            
            # Se verifica que el nombre ingresado se encuentre en el arreglo de clientes
            if nombreCliente in self.nombresClientes:
                cliente_socket.sendall("Eliga su opción:\n".encode())
                cliente_socket.sendall("1. Partido A\n".encode())
                cliente_socket.sendall("2. Partido B\n".encode())
                cliente_socket.sendall("3. Partido C\n".encode())
                cliente_socket.sendall("4. Ninguno\n".encode())

                # Se espera la respuesta del cliente
                opcion = cliente_socket.recv(1024).decode().strip()
                print(f"El {nombreCliente} eligió la opción {opcion}")
                cliente_socket.sendall("Gracias por tu voto\n".encode())
                
            else:
                cliente_socket.sendall("No te encuentras registrado en el sistema\n".encode())
                cliente_socket.sendall("Hasta pronto\n".encode())
                cliente_socket.close()

        except ConnectionResetError:
            print("El cliente ha cerrado la conexión inesperadamente")

        # Aquí podría ir una actualización de los votos de los clientes 
        
    def iniciaServidor(self):
        # Configuración del servidor
        host = "localhost"
        port = 4000

        # Variable que almacena el socket, que será TCP
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enlace con host y puerto
        servidor_socket.bind((host,port))
        # Conexiones entrantes
        servidor_socket.listen(10)
                
        while True:
            # Se espera las conexiones
            cliente_socket, direccion = servidor_socket.accept()
            # Hilo para manejar la conexión 
            cliente_thread = threading.Thread(target=self.manejarCliente, args=(cliente_socket, direccion))
            cliente_thread.start()

# Inicializando el servidor
if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciaServidor()

