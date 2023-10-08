import socket


def scanner():

    for port in range(4995, 5006):

        #TCP
        client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #AF_INT = ipv4 SOCK_STREAM for TCP

        host = socket.gethostname() #modify for target ip
         #modify for target port

        try:
            #print(f"Connection to {host}:{port}...")
            client.connect((host,port))
            #print(f"Connected to {host}:{port}, grabbing header")
            message = client.recv(1024)
            #print(f"Received from {host}:{port}")
            client.close()
            #print(f"Closed connection with {host}:{port}")

            #print("Received from {}:{} : {}".format(host,port,message))
            if message != None:
                print(f"Le port {port} est ouvert pour une connection TCP")
        except socket.error as err:
            print(f"Le port {port} n'est pas ouvert pour une connection TCP")
            client.close()
            #UDP
            client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #AF_INT = ipv4 SOCK_DGRAM for udp

            host = socket.gethostname() #modify for target ip
            #modify for target port
            client.settimeout(5.0)

            #print(f"Sending UDP to {host}:{port}")
            client.sendto(b'Banner query\r\n',(host,port))
            try:
                #print(f"Waiting for response...")
                message = client.recvfrom(1024)
                #print(f"Received from {host}:{port} : {message}")
                if message != None:
                    print(f"Le port {port} est ouvert pour une connection UDP")
            except socket.timeout:
                print(f"Le port {port} n'est pas ouvert pour une connection UDP")
        finally:
            client.close()
    
print(scanner())
