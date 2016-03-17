import socket

import sys

host = "pythonprogramminglanguage.com"
port = 80

print('Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Fail to create socket")
    sys.exit()

print("# Getting remote IP address")
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

print("Connection to server: " + host + " | IP = " + remote_ip)
s.connect((remote_ip,port))

request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print("Cannot send")
    sys.exit()

print("# Received from server: ")
reply = s.recv(4096)

print(reply)




