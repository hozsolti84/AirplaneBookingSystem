from DB.connection import Connections
# todo: clearify this *
from exceptions.exceptions import *
from utils.utils import get_data

class AirplaneAction:

    # table = "airplanes" # todo: delete this, if the table name stays it unnecessary
    section = "query"

    def __init__(self, model=None, registration=None, capacity=None):
        self.model = model
        self.registration = registration
        self.capacity = capacity
        self.connection = Connections().create_connection()

    def get_query(self, action):
        try:
            base_query = get_data(AirplaneAction.section, action)
            return base_query
        # todo: make more specific exceptions can it been done with decorators?
        except Exception as e:
            print(e)

    def make_query(self, action):
        query = get_data(AirplaneAction.section, action)
        action = action.split("_")[1]
        print('DELETE THIS: action = action.split("_")[1]: ', action)
        if action == "select":
            params = (self.registration,)
        #todo: should be an else, this only for testing purposes:
        elif action in ("insert", "update", "delete"):
            params = (self.model, self.registration, self.capacity)

        return query, params

    def query_executer(self, action="select"):
        query, params = self.make_query(action)
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

    def select_plain(self):
        res = self.query_executer(action="select")
        # todo: put info here for the log
        if res:
            return res[0]
        else:
            return []

    def create_plain(self):
        self.query_executer("insert")

    def update_plain(self):
        self.query_executer("update")

    def remove_plain(self):
        self.query_executer("delete")

    def select_all_plains(self):
        pass


if __name__=='__main__':
    airplain = AirplaneAction()
    airplain.select_plain()

