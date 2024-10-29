import socket

# Message handling in seperate threads for each client connecting to our server
# Client doesnt wait for another client to send/receive message before its able to access server
import threading

PORT = 5050

# Use this to retreive the IPv4 address of CSE
SERVER = socket.gethostbyname(socket.gethostname())

# Binding socket to specific address as a tuple
ADDR = (SERVER, PORT)

# Tells socket what type of IP address we will be looking for for specific connections, INET = IPv4, INET6 = IPv6
# AF_INET = Over the internet, specify type of address we are looking for
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bounded above socket to ADDR (address)
server.bind(ADDR)
