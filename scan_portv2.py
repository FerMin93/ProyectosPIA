#America Fernanda Martinez Barron 
#Matricula: 1901395

import socket

def scan(addr, port):
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(1)

    results = socket_obj.connect_ex((addr, port))

    socket_obj.close()

    return results

ports = [21, 22, 25, 80]

for i in range(1, 255):
    addr = '192.168.1.{}'.format(i)
    for port in ports:
        result = scan(addr, port)
        if result == 0:
            print(addr, port, 'OK')
        else:
            print(addr, port, 'Failed')
        
