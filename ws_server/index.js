const http = require('http');
const socketClusterServer = require('socketcluster-server');

let httpServer = http.createServer();
let agServer = socketClusterServer.attach(httpServer);

(async () => {
	let myTokenData = {
		username: 'bob',
		language: 'English',
		company: 'Google',
		groups: ['engineering', 'science', 'mathematics'],
	};

	// agServer.signatureKey below is the key which SocketCluster uses to sign the token.
	// By default, agServer.signatureKey is equal to agServer.options.authKey
	// (and also equal to agServer.verificationKey); but these may differ if you
	// switch to a different JWT algorithm in the future.

	let signedTokenString;
	try {
    signedTokenString = await agServer.auth.signToken(myTokenData, agServer.signatureKey);
    console.log({signedTokenString});
	} catch (error) {
		// ... Handle failure to sign token.
		return;
	}
})();

async function connect() {
	for await (let { socket } of agServer.listener('connection')) {
		console.log('Socket is connected');
		for await (let data of socket.receiver('customRemoteEvent1')) {
			console.log(data);
		}
	}
}

connect();
httpServer.listen(8001);
