const socketClusterClient = require('socketcluster-client');

let options = {
	port: 8001,
	hostname: 'localhost',
	autoConnect: true,
	secure: false,
	rejectUnauthorized: false,
	connectTimeout: 10000, //milliseconds
	ackTimeout: 10000, //milliseconds
	channelPrefix: null,
	disconnectOnUnload: true,
	autoReconnectOptions: {
		initialDelay: 10000, //milliseconds
		randomness: 10000, //milliseconds
		multiplier: 1.5, //decimal
		maxDelay: 60000, //milliseconds
	},
	authEngine: null,
	codecEngine: null,
};

let agClientSocket = socketClusterClient.create(options);

(async () => {
	console.log("listen chanel");
	let channel = agClientSocket.subscribe('yell');
	for await (let data of channel) {
		console.log(data);
	}
})();

(async () => {
	console.log("listen");
	for await (let {socket} of agClientSocket.listener('connection')) {
		console.log('Socket is connected');
		for await (let data of socket.receiver('customRemoteEvent1')) {
			console.log(data);
		}
	}
})();
