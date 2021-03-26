# Based on the following tutorial: https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
import socket
import main as m

class ourServer():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def openCloseConnection(self, connectionInfo):
        self.sock.bind(connectionInfo) # Bind to an address to recive client responses
        self.sock.listen(1) # Get one clinet
        conn, addr, = self.sock.accept()

        loaded_clf = m.load_sentiment_analysis()[0]
        while(True): # While we still get valid responses from our 1 client
            clientResponse=self.getResponse(conn)
            if not clientResponse: # If the data we got is empty or terminating condition
                break

            print("Client message: " + clientResponse)
            response = m.getFinalOutput(loaded_clf, clientResponse)

            if clientResponse == "quit":
                response = "Goodbye!"
            self.sendResponse(response, conn)
        conn.close()
        print("We've lost our client")

    def getResponse(self, conn):
        return conn.recv(4096).decode("utf-8")
    
    def sendResponse(self, msg, conn):
        conn.send(bytes(msg.encode()))
    
    def runServer(self):
        ip = socket.gethostname()
        port = int(input("enter target port: "))
        server.openCloseConnection((ip, port))

if __name__ == "__main__":
    server = ourServer()
    server.runServer()
