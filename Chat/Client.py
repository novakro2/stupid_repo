#!/usr/bin/python           # This is client.py file
from socketIO_client import SocketIO, LoggingNamespace

host = "69.176.142.67"       # Get local machine name
port = 3000               # Reserve a port for your service.

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO(host, port, LoggingNamespace) as socketIO:
    socketIO.on('Hey!', on_bbb_response)
    socketIO.emit('chat message', "Hey!", on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)
