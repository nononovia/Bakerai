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
    
    def runClient(self):
        ip = input ("enter target IP Address: ")
        port = int(input("enter target port: "))
        client.connect((ip, port)) 
        userInput = ""
        while userInput != "quit":
            userInput = input("Send a message: ")
            client.sendResponse(userInput)
            response = client.getResponse()
            print("Server response: " + response)
        client.close()

if __name__ == "__main__":
    client = ourClient()
    client.runClient()
    