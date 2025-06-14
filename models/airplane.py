from repository.airplane_repo import AirplaneAction

class Airplane:
    """Defines a specific aircraft model and its seating."""
    def __init__(self, model: str = None, registration: str = None, capacity: int = None):
        """
        :param model: e.g., “Airbus A320”
        :param registration: tail number
        :param capacity:
        :param seat_map: {seat_number: None | Passenger}e.g., {'1A': None, '1B': Passenger(...), ...}
        """
        self.__model = model
        self.__registration = registration
        self.__capacity = capacity

    @property
    def model(self):
        return self.__model

    @property
    def registartion(self):
        return self.__registration

    def set_registration(self, registration):
        self.__registration = registration

    @property
    def capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        pass

    def check_airplane(self):
        plain_in_DB = AirplaneAction().query_executer()
        if self.registartion in plain_in_DB:
            print(f"model: {self.__model}"
                  f"registration: {self.__registration}"
                  f"capacity: {self.__capacity}")

    def create_plain(self, ):
        """INSERT INTO {} (model, registration, capacity) VALUES (%s, %s, %s, %s)"""
        plain_in_DB = AirplaneAction()



if __name__=='__main__':
    plane = Airplane("Airbus 100", "A00002", 100)

