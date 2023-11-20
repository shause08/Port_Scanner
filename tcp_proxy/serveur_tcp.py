import socket

# Configuration du serveur
server_port = 8888

# Création d'une socket pour le serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', server_port))
server_socket.listen(1)

print(f"Le serveur est à l'écoute sur le port {server_port}")

# Attente de la connexion d'un client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Attente de données du client
data_from_client = client_socket.recv(1024)
print(f"Reçu du client : {data_from_client.decode()}")

# Envoi des données au client
response_to_client = "Bonjour, client!"
client_socket.send(response_to_client.encode())

# Fermeture des connexions
client_socket.close()
server_socket.close()
