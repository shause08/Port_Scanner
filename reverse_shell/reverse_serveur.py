import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #AF_INT = ipv4

host = socket.gethostname()
port = 5000

server_socket.bind((host,port))
server_socket.listen(5)

print(f"Execution du serveur TCP sur {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

while True:
    command_to_execute = input("Entrez une commande (ou tapez 'QUIT' pour terminer la connexion): ")

    client_socket.sendall(command_to_execute.encode('utf-8'))

    if command_to_execute.upper() == 'QUIT':
        break

    client_response = client_socket.recv(1024).decode('utf-8')
    print(f"Réponse du client : {client_response}")

print("Fermeture de la connexion...")
client_socket.close()
server_socket.close()

