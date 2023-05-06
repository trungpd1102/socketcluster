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


agClientSocket.transmitPublish('yell', JSON.stringify({ name: 'Trung', age: 28 }));
agClientSocket.transmit('customRemoteEvent1', JSON.stringify({ name: 'Trung', age: 28 }));

