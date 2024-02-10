import sys
import socket


ip = input("Enter you ip address: ")
domain_name = socket.gethostbyname(ip)

open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # another_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")
























  '''
import socket
import datetime

try:
    def scanning_ports(ipaddress, starting_port, ending_port):
        for port in range(starting_port, ending_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ipaddress, port))
            if result == 0:
                print(f"Port {port} is open")
                grabbing_banners(ipaddress, port)
            sock.close()

    def grabbing_banners(ipaddress, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ipaddress, port))
            banner = sock.recv(1024)
            print(f"Banner for {ipaddress}:{port} - {banner.decode()}")
            sock.close()
        except Exception as e:
            pass

    domain_name = input("Enter domain name/ip address: ")
    ipaddress = socket.gethostbyname(domain_name)

    print('=' * 51)
    print(f"Started port scanning at {datetime.datetime.now()}")
    print('=' * 51)
    scanning_ports(ipaddress, 1, 65535)

except KeyboardInterrupt:
    print("\n Keyboard Interrupt")
  
  '''