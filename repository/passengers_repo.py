from utils.utils import get_data
from DB.connection import Connections
from exceptions.exceptions import GetdataExceptionError


class PassengerActions:
    def __init__(self,
                 passport_number=None,
                 name=None,
                 email=None,
                 field=None,
                 reservations=None,
                 frequent_flyer_points=0,
                 new_value=None,
                 old_value=None,
                 table="passengers"):  # todo: Here the table="passengers" is possibly if it is the only table being used
        self.passport_number = passport_number
        self.name = name
        self.email = email
        self.field = field
        self.reservations = reservations
        self.frequent_flyer_points = frequent_flyer_points
        self.new_value = new_value
        self.table = table
        self.base_query = None
        self.query = None
        self.params = None # used for to format the SQL CRUD strings.
        self.old_value = old_value
        self.connection = Connections().create_connection()


    # todo: Rewrite the get_query() like this to avoid possible SQL injections.
    def get_query(self, action="select"):
        """getting the sql base query from the config.ini"""
        try:
            base_query = get_data("query", action)
        except GetdataExceptionError as gee:
            print(gee)
        if action == "select":
            query = base_query #.format(self.table)  # todo: If only one table is used this can be removed, because only the table is being introduced here
            params = (self.passport_number,)
        # if action == "update":
        #     query = base_query.format(self.table)
        #     params = (self.passport_number, self.field, self.new_value, self.old_value)
        if action in ("insert", "delete"):
            query = base_query.format(self.table)
            params = (self.name, self.email, self.passport_number, self.frequent_flyer_points)

        return query, params


    def query_executer(self, action="select"):
        query, params = self.get_query(action)
        print("query: ", query) # todo: delete this
        print("params: ", params)  # todo: delete this
        cur = self.connection.cursor()
        try:
            cur.execute(query, params)
            if action == "select":
                res = cur.fetchall()
                return res
            elif action in ("insert", "delete", "update"):
                print("else have been triggered!")
                self.connection.commit()
                print("commit have been triggered!")
                if cur.rowcount > 0:
                    print(f"The '{action}' was successful for {self.passport_number}")
                else:
                    print(f"The '{action}' was UNSUCCESSFUL for {self.passport_number}")
        except Exception as e:
            print(f"An exception has occurred during the SQL query '{query}'")
            print(e)
            print("query", query)
            print("params", params)
        finally:
            """
            ensures the cursor and connection are closed even if an exception occurs,
            preventing memory leaks and locked resources.
            """
            cur.close()
            self.connection.close()

    def select_passenger(self):
        res = self.query_executer()
        # todo: put info here for the log
        if res:
            return res[0]
        else:
            return []

    def create_passenger(self, action):
        self.query_executer(action)


    def update_passenger(self): pass

    def remove_passenger(self): pass

    def get_passenger_list(self): pass


if __name__=="__main__":
    # andor = PassengerActions('A23456789')
    # a1 = andor.select_passenger()
    # print(a1)
#                           self.name, self.email, self.passport_number, self.frequent_flyer_points
    balazs = PassengerActions(name="Csaba", email="csaba@gmail.com", passport_number="000012", frequent_flyer_points=0)
    balazs.create_passenger("insert")
