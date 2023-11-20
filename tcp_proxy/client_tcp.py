import socket

# Configuration du client
proxy_address = ('localhost', 9999)

# Création d'une socket pour le client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(proxy_address)

# Envoi des données au proxy
data_to_proxy = "Hello, proxy!"
client_socket.send(data_to_proxy.encode())
print(f"Envoyé au proxy : {data_to_proxy}")

# Attente de la réponse du proxy
response_from_proxy = client_socket.recv(1024)
print(f"Reçu du proxy : {response_from_proxy.decode()}")

# Fermeture de la connexion
client_socket.close()
