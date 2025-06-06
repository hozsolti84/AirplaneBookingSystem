import mysql.connector
from utils.utils import get_data


class Connections:
    # todo: do I need this init?
    # def __init__(self):
    #     pass

    @staticmethod
    def get_connection_data():
        # path = "../config.ini"
        """create a connection with DB.connection.get_connection()"""
        # todo: the path, "db" and the "host", "port", "user", "password" should be imported from the config.ini
        # todo :e.g. config.ini
        host = get_data( "db","host")
        port = get_data("db", "port")
        user = get_data("db", "user")
        password = get_data("db", "password")
        database = get_data("db", "database")
        print("The connection is being established for:")
        print("========================================")
        print("host:", host)
        print("port:", port)
        print("user:", user)
        print("password:", "************")
        print("database:", database)

        return host, port, user, password, database

    @staticmethod
    def create_connection():
        # todo: the query should not be executed here
        """     0      1    2       3
        *args: host, port, user, password
        :returns connection to the DB - the execution can be found in the e.g. repository.passenger_repo
        """
        args = Connections.get_connection_data()
        # Connect to server
        try:
            connection = mysql.connector.connect(
                host=args[0],
                port=int(args[1]),
                user=args[2],
                password=args[3],
                database=args[4]
            )
        except (ConnectionAbortedError,
                ConnectionRefusedError,
                ConnectionResetError,
                ConnectionError) as e:
            raise e

        return connection

