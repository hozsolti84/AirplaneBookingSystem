import mysql.connector

def get_connection(*args):
    # todo: the query should not be executed here
    """     0      1    2       3
    *args: host, port, user, password
    :returns connection to the DB - the execution can be found in the e.g. repository.passenger_repo
    """
    # Connect to server
    try:
        connection = mysql.connector.connect(
            host=args[0],
            port=int(args[1]),
            user=args[2],
            password=args[3]
        )
    # todo: make
    except ConnectionAbortedError as CAE:
        raise CAE
    except ConnectionRefusedError as CRefE:
        raise CRefE
    except ConnectionResetError as CResE:
        raise CResE
    except ConnectionError as CE:
        raise CE

    return connection
