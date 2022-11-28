import socket
import handleFunc

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65431        # The port used by the server
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)
#se
try:
    while True:
        data = s.recv(1024)
        print('Server: ', data.decode("utf8"))
        msg = input('Client: ')
        s.sendall(bytes(msg, "utf8"))
        
        if msg == "Quit":
            break

        if msg == "View menu":
            handleFunc.viewMenu()
            continue
        
finally:
    print('closing socket')
    s.close()
