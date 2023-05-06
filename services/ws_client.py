from socketclusterclient import Socketcluster
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class SocketclusterClient:
    socket_client = None
    ag_socket = None
    channel = None
    
    app = None
    host = None
    post = None

    def onconnect(self, socket):
        logging.info("on connect got called")
        self.ag_socket = socket
        print('run app')
        self.app.run(host=self.host, port=self.port, debug=True)

    def ondisconnect(self, socket):
        logging.info("on disconnect got called")

    def on_connect_error(self, socket, error):
        logging.info("On connect error got called")

    def subscribe_channel(self, channel):
        self.channel = channel
        self.ag_socket.subscribe(channel)

    def publish_via_channel(self, data):
        self.ag_socket.publish(self.channel, data)

    def init_app(self):
        self.socket_client = Socketcluster.socket(
            "ws://localhost:8001/socketcluster/")
        self.socket_client.setBasicListener(
            self.onconnect, self.ondisconnect, self.on_connect_error)

    def run(self, app, host=None, port=None):
        self.host = host
        self.port = port
        self.app = app
        print('connect')
        self.socket_client.connect()
