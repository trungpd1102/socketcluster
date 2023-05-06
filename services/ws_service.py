from socketclusterclient import Socketcluster
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class SocketclusterClient:
    socket_client = None
    ag_socket = None
    channel = None

    content = None

    def onconnect(self, socket):
        logging.info("on connect got called")
        socket.subscribe(self.channel)
        socket.publish(self.channel, self.content)
        self.socket_client.disconnect()

    def ondisconnect(self, socket):
        logging.info("on disconnect got called")

    def on_connect_error(self, socket, error):
        logging.info("On connect error got called")
        raise ValueError('Socket connection error', error)

    def init_app(self):
        print('inint app')
        self.socket_client = Socketcluster.socket(
            "ws://localhost:8001/socketcluster/")
        self.socket_client.setBasicListener(
            self.onconnect, self.ondisconnect, self.on_connect_error)
        self.socket_client.connect()

    def publish_via_channel(self, channel=None, content=None):
        self.channel = channel
        self.content = content
        self.init_app()

    def __del__(self): 
        print("Destructor called, SocketclusterClient deleted.") 
        self.socket_client.disconnect()

