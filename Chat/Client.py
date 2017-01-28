#!/usr/bin/python           # This is client.py file
from socketIO_client import SocketIO, LoggingNamespace

host = "10.255.6.96"       # Get local machine name
port = 3000               # Reserve a port for your service.


def on_login_response():
    print("Sending message...")
    socketIO.emit('new message', 'weather')


def on_message_response():
    print("Disconnecting...")
    socketIO.disconnect()


with SocketIO(host, port, LoggingNamespace) as socketIO:
    socketIO.on('login response', on_login_response)
    socketIO.on('got message', on_message_response)

    print("Sending login request...")
    socketIO.emit('login')
    socketIO.wait(seconds=1)



