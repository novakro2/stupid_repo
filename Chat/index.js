var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var ip = require('ip');



io.on('connect', function(socket){
	console.log('initial connection received...');
	socket.on('login', function(){
		console.log('connected');
		io.sockets.emit('login response');
	});
	
	socket.on('new message', function(data){
		console.log('new message: %s', data);
		io.sockets.emit('new message', { jimmy: data });
		socket.emit('got message');
	});
	
});

http.listen(3000, ip.address(), function(){
  console.log('listening on %s:3000', ip.address());
});
