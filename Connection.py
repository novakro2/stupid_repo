import sys
import pymysql
import pymysql.cursors
from sshtunnel import SSHTunnelForwarder

def sqlconnect():
    connection = pymysql.connect(
            host='updatedb.cokzgjg547m0.us-east-1.rds.amazonaws.com',
            user='update_user',
            password='HelloWorld',
            database="updatedb",
            port=3306
        )
    return connection

sqlconnect()


