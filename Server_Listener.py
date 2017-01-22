import socket
import json
from threading import *
from requests import Request, Session
from Connection import *


# Create the query to get the desired data from the database
# param: req The request the user is asking for
# param: action Is the user trying to add or search the database
def sql_query(req, action):
    try:
        connection = sqlconnect()
        cursor = connection.cursor()
    except:
        print("Connection to db failed...")
    print(req)
    try:
        if action == "pull":
            # SQL query to pull all network_locations and JSON_data from network_locations_JSON
            sql = """SELECT * from test_data
            WHERE activity_cat1 like "%{}%" OR
            activity_name like "%{}%"
            OR activity_description like "%{}%"
            """.format(req, req, req)


        elif action == "push":
            sql = """INSERT INTO test_data (activity_cat1, activity_name, activity_organizer, activity_street,
            activity_city, activity_state, activity_zip, activity_description, activity_country)
            VALUES {}""".format(req)

            sql2 = """Select * from test_data WHERE p_id = 30"""
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            print(result2)

        cursor.execute(sql)
        result = cursor.fetchall()

        print("The query is: ", sql)
        print(result)
        dict_str = { "data" : {} }
        for row in result:
            dict_str["data"][row[0]] = row[1:]

        print(dict_str)
        json1 = json.dumps(dict_str)
        print(json1)

    except ERROR as err:
        print("SQL failed...", err)
        # Close connections
        cursor.close()
        connection.close()
    cursor.close()
    connection.close()

    return dict_str


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
        client_req = self.sock.recv(1024).decode().split('?')
        print('Client sent:', client_req)
        # Split the client request into two parts
        query = client_req[0]
        action = client_req[1]
        # Perform the sql query
        result = sql_query(query, action)
        self.sock.send(bytes(json.dumps(result), "utf-8"))
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


