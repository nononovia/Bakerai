# Based on the following tutorial: https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
import socket
class ourServer():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def openCloseConnection(self):
        self.sock.bind(("127.0.0.1", 8080)) # Bind to an address to recive client responses
        self.sock.listen(1) # Get one clinet
        conn, addr, = self.sock.accept()

        while(True): # While we still get valid responses from our 1 client
            clientResponse=self.getResponse(conn)
            if not clientResponse: # If the data we got is empty
                break

            print(clientResponse)
            self.sendResponse("Server response:", conn)
        conn.close()
        print("We've lost our client")

    def getResponse(self, conn):
        return conn.recv(4096).decode("utf-8")
    
    def sendResponse(self, msg, conn):
        conn.send(bytes(msg.encode()))

if __name__ == "__main__":
    server = ourServer()
    server.openCloseConnection()