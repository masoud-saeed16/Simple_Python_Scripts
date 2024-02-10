import socket

try:
    def scanning_ports(ipaddress, starting_port, ending_port):
        for port in range(starting_port, ending_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ipaddress, port))
            if result == 0:
                print(f'Port {port} is open')
                grabbing_banners(ipaddress,port)
            sock.close()

    def grabbing_banners(ipaddress,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ipaddress,port))
            banner = sock.recv(1024)
            print(f'Banner for {ipaddress}:{port} is {banner.decode()}')
            sock.close()
        except Exception as e:
            print(e)

    ipaddress = input("Enter your ipaddress: ")
    domain_name = socket.gethostbyname(ipaddress)
    scanning_ports(ipaddress,1,65535)
except KeyboardInterrupt:
    print("Program Closed")

