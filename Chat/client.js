var io = require('socket.io-client');
var socket = io.connect('http://10.255.6.96:3000', {reconnect: true});

data = 'test'
socket.on('login response', function(){
	socket.emit('new message', data); //send user_request to the server
});

socket.on('got message', function() {
	console.log("Disconnecting")
	socket.disconnect();
});
		
	
socket.emit('login');