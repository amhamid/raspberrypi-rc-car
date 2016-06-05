from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import car_control_mock as car_control


class SimpleWebSocket(WebSocket):
    def handleMessage(self):
        print self.data
        if self.data == 'forward':
            car_control.forward()
        elif self.data == 'backward':
            car_control.backward()
        elif self.data == 'left':
            car_control.left()
        elif self.data == 'right':
            car_control.right()
        elif self.data == 'cleanup':
            car_control.cleanup()
        else:
            car_control.cleanup()

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'


server = SimpleWebSocketServer('', 9090, SimpleWebSocket)
server.serveforever()
