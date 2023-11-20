import socket

# Configuration du proxy
proxy_port = 9999
destination_address = ('localhost', 8888)

# Création d'une socket pour le proxy
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.bind(('0.0.0.0', proxy_port))
proxy_socket.listen(1)

print(f"Le proxy est à l'écoute sur le port {proxy_port}")

# Attente de la connexion d'un client
client_socket, client_address = proxy_socket.accept()
print(f"Connexion établie avec {client_address}")

# Connexion à la destination
destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination_socket.connect(destination_address)

# Envoi des données du client à la destination
destination_socket.sendall(client_socket.recv(1024))

# Attente de la réponse de la destination
data_from_destination = destination_socket.recv(1024)
print(f"Reçu de la destination : {data_from_destination.decode()}")

# Envoi de la réponse au client
client_socket.sendall(data_from_destination)

# Fermeture des connexions
client_socket.close()
destination_socket.close()
proxy_socket.close()