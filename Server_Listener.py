import socket
import json
from threading import *
from requests import Request, Session
from Connection import *


# Create the query to get the desired data from the database
def sql_query():
    try:
        connection = sqlconnect()
        cursor = connection.cursor()
    except:
        print("Connection to db failed...")

    try:
        # SQL query to pull all network_locations and JSON_data from network_locations_JSON
        sql = """SELECT * from test_data"""
        cursor.execute(sql, )
        result = cursor.fetchall()

        for row in result:
            print(row)
    except:
        print("SQL failed...")
        # Close connections
    cursor.close()
    connection.close()

    return result


# How to hande the client socket after it's been accepted
class client(Thread):

    # Called when the client is initialized
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    # Called when start is called
    def run(self):
        print('Client sent:', self.sock.recv(1024).decode())
        result = sql_query()
        self.sock.send(bytearray(json.dumps(result), 'utf8'))
        self.sock.shutdown(socket.SHUT_WR)
        self.sock.close()

def main():

    #create an INET, STREAMing socket
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to a public host,
    # and a well-known port
    serversocket.bind((socket.gethostname(), 8085))
    #become a server socket
    serversocket.listen(5)

    while 1:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # create a client and go back to listening
        client(clientsocket, address)
main()


