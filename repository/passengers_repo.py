
from DB.connection import get_connection
from utils.utils import get_data


def select_passenger(passport_number, table="passengers"):
    """gets one passenger or passenger list"""
    query = get_data("config.ini", "query", "select").format(passport_number, table)

    """create a connection with DB.connection.get_connection()"""
    host = get_data("config.ini", "db", "host")
    port= get_data("config.ini", "db", "port")
    user = get_data("config.ini", "db", "user")
    password = get_data("config.ini", "db", "password")
    connection = get_connection(host, port, user, password)
    print("host:", host)
    print("port:", port)
    print("user:", user)
    print("password:", password)

    cur = connection.cursor()

    """Execute a query"""
    print(f"The query '{query}' is being executed!")
    cur.execute(query)

    """"check results"""
    for row in cur:
        print(row)

    # Close connection
    connection.close()

def insert_passener(query): pass

def delete_passenger(query): pass

if __name__=="__main__":
    select_passenger('12345678')