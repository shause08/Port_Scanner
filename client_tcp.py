import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #AF_INT = ipv4 SOCK_STREAM for TCP

host = socket.gethostname() #modify for target ip
port = 5000 #modify for target port

print(f"Connection to {host}:{port}...")
client.connect((host,port))
print(f"Connected to {host}:{port}, grabbing header")
message = client.recv(1024)
print(f"Received from {host}:{port}")
client.close()
print(f"Closed connection with {host}:{port}")

print("Received from {}:{} : {}".format(host,port,message))
