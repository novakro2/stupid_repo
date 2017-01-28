var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var ip = require('ip');



io.on('connection', function(socket){
	socket.on('chat message', function(msg){
		console.log('message: ' + msg);
		socket.emit(msg)
  });
});

http.listen(3000, ip.address(), function(){
  console.log('listening on *:3000');
});