import socket
import datetime
import concurrent.futures

def scanning_ports(ipaddress, starting_port, ending_port):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(scan_port, ipaddress, port): 
                    port for port in range(starting_port, ending_port + 1)}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                result = future.result()
                if result == 0:
                    print(f"Port {port} is open")
                    open_ports.append(port)
                    grabbing_banners(ipaddress, port)
            except Exception as e:
                pass
    return open_ports

def scan_port(ipaddress, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        return sock.connect_ex((ipaddress, port))

def grabbing_banners(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((ipaddress, port))
            banner = sock.recv(1024)
            print(f"Banner for {ipaddress}:{port} - {banner.decode()}")
    except Exception as e:
        pass

try:
    domain_name = input("Enter domain name/ip address: ")
    ipaddress = socket.gethostbyname(domain_name)

    print('=' * 51)
    print(f"Started port scanning at {datetime.datetime.now()}")
    print('=' * 51)

    choice = input("Choose scanning option (1 for first 1024 ports, 2 for all ports): ")

    def scan_first_1024_ports(ipaddress):
        return scanning_ports(ipaddress, 1, 1024)

    def scan_all_ports(ipaddress):
        return scanning_ports(ipaddress, 1, 65535)

    if choice == '1':
        open_ports = scan_first_1024_ports(ipaddress)
    elif choice == '2':
        open_ports = scan_all_ports(ipaddress)
    else:
        print("Invalid choice. Exiting.")
        exit()

    # if open_ports:
    #     print("Open ports:", open_ports)
    # else:
    #     print("No open ports found.")

except KeyboardInterrupt:
    print("\n Keyboard Interrupt")
