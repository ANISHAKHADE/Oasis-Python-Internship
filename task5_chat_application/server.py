import socket

def chas():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1",3000))
    server.listen(1)
    print("Server is listening...")
    conn, addr = server.accept()
    print(f"Conneted by  {addr} ")

    while True:
        data=conn.recv(1024)

        if not data:
            print("No data received")
            break

        msg=data.decode()
        print("Client:",msg)

        if msg.lower()=="exit" or msg.lower()=="quit":
            print("Goodbye!".encode())
            break
        
        
        # conn.send("Hello".encode())


        reply=input("Server:")
        conn.send(reply.encode())

    conn.close()
    server.close()


chas()
