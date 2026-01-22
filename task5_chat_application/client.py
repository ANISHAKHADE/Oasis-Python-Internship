import socket

def chac():
    
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1",3000))

    while True:
        msg=input("You:")
        client.send(msg.encode())
        data=client.recv(1024)
        print("Server :", data.decode())

        if msg.lower()=="exit" or msg.lower()=="quit":
            # print("Goodbye!".encode())
            break

    client.close()


chac()



 
