#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    testing_port = min_port
    testing_address = address
    temp_socket = socket.socket()

    
    while testing_port <= max_port:
        try:
            temp_socket.connect((testing_address,testing_port))
            found_ports.append(testing_port)
            testing_port = testing_port+1
        except:
            testing_port = testing_port+1 
    
    return found_ports


def main(argv):
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
