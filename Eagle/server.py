from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response


class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print(self.address, 'start')
        message = self.data
        print(self.address, 'step1:'+message)
        response = get_response(message)
        print(self.address, 'step4:'+response)
        self.sendMessage(response)
        print(self.address, 'handle')

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
