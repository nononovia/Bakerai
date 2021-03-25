# Based on the following tutorial: https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
import socket
class ourServer():
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0",8080)) # Bind to an address to recive client responses
        sock.listen(10)
        while(True):
            conn, addr, = sock.accept()
            clientStr = ""

            while(True):
                data=conn.recv(4096)
                if not data: break
                clientStr += data
                print(clientStr)
                conn.send("Server response \n")
            conn.close()
            print("We've lost our client")