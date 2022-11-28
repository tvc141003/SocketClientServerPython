import socket
import threading
import handleFunc
import definedObj

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1000)

# foodMenu = [
#     Food("That Salads", 10, "Salads and soup", "").getFood(),
#     Food("Spinach and Ricotta", 20, "A vegan", "").getFood(),
#     Food("Beefsteak", 60, "Mains", "").getFood(),
#     Food("Pasta with Prawns", 15, "Pasta", "").getFood(),
#     Food("Chocolate Lava Cake", 10, "Dessert", "").getFood(),
# ]

def handleConnect(client):
    global count
    try:
        print('Connected by', client.addr)
        handleFunc.welcomeClient(client)
        
        while True:
            data = client.conn.recv(1024)
            str_data = data.decode("utf8")
            if (str_data == "Quit"):
                msg = "Type any chbcaracters to quit!"
                client.conn.sendall(bytes(msg, "utf-8"))
                break
            """if not data:
                break
            """
            print("Client: " + str_data)
            if (str_data == "Count connected people"):
                msg = f"Number of people to connect server: {count}"
                client.conn.sendall(bytes(msg+'\nAny request?', "utf8"))
                continue

            if (str_data == "View menu"):
                client.conn.sendall(bytes('\nAny request?', "utf8"))
                #handleFunc.viewMenu(client)
                continue
            
            if (str_data == "View port"):
                msg = f"Port is: {client.addr[1]}"
                client.conn.sendall(bytes(msg+'\nAny request?', "utf-8"))
                continue
            
            if (str_data == "Order food"):
                handleFunc.orderFood(client)
                continue

            if (str_data == "Pay bill"):
                handleFunc.payBill(client)
                continue
                
            if (str_data == "Add food"):
                handleFunc.addFood(client)
                continue

            # Server send input
            msg = "Invalid!"
            client.conn.sendall(bytes(msg, "utf8"))
    finally:
        # Clean up the connection
        count = count - 1
        client.conn.close()
        # if count == 2: 
        #     break

count = 0
while True:
    conn, addr = s.accept()
    count += 1
    createClient = definedObj.Client(conn, addr)
    # print(createClient.conn, createClient.addr)
    threadClient = threading.Thread(target=handleConnect, args = (createClient,))
    threadClient.start()

s.close()