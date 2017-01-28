var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var ip = require('ip');



io.on('connect', function(socket){
	socket.on('login', function(){
		console.log('connected');
		socket.emit('login response');
	});
	
	socket.on('new message', function(data){
		console.log('new message: %s', data);
		socket.emit('got message')
		socket.emit(data);
	});
	
});

http.listen(3000, ip.address(), function(){
  console.log('listening on %s:3000', ip.address());
});