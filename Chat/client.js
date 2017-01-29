var io = require('socket.io-client');
var socket = io.connect('http://54.80.151.86:8085', {reconnect: true});

data = 'test'
socket.on('login response', function(){
	socket.emit('new message', data); //send user_request to the server
});

socket.on('got message', function() {
	console.log("Disconnecting")
	socket.disconnect();
});
		
	
socket.emit('login');