import socket
class ourClient():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self, connectInfo):
        self.sock.connect(connectInfo)
    
    def getResponse(self):
        return self.sock.recv(4096).decode("utf-8")

    def sendResponse(self, msg):
        self.sock.send(bytes(msg.encode()))
    
    def close(self):
        self.sock.close()

if __name__ == "__main__":
    client = ourClient()
    client.connect(("127.0.0.1", 8080)) 
    userInput = ""
    while userInput != "quit":
        client.sendResponse(input("Send a message: "))
        response = client.getResponse()
        print(response)
    client.close()