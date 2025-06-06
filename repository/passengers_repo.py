from utils.utils import get_data
from DB.connection import Connections
class PassengerActions:
    def __init__(self, passport_number, table="passengers"):
        self.passport_number = passport_number
        self.table = table
        self.query = get_data("query", "select").format(table, passport_number)
        self.connection = Connections().create_connection()

    def get_query(self):
        self.query = get_data("query", "select").format(self.table, self.passport_number)
        return self.query

    def query_executer(self):
        self.query = self.get_query()
        print(f"The query '{self.query}' is being executed!")
        cur = self.connection.cursor()
        cur.execute(self.query)
        res = cur.fetchall()
        self.connection.close()

        return res


    def select_passenger(self):
        """Execute a query"""
        res = self.query_executer()
        print("res: ", res)

        """"check results"""
        "This is from the Passenger.PassengerActions.select.passenger()"
        if res:
            return res[0]
        else:
            print(f"No result was found for the passanger with passport number '{self.passport_number}'")


    def insert_passenger(self): pass


    # todo: use this too if you can.
    def update_passenger(self): pass

    def delete_passenger(self): pass

    # todo: do I need this here or will I call it somehow else?
    def get_passenger_list(self): pass


if __name__=="__main__":
    andor = PassengerActions('A23456789')
    andor.select_passenger()