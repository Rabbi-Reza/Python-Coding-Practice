import socket as s
# host = 'www.google.com'
host = input("Insert website address: ")
print(f'IP of {host} is {s.gethostbyname(host)}')
