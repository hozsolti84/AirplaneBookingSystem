from models.airplane import Airplane
from models.person import Passenger
from repository.passengers_repo import PassengerActions
from exceptions.exceptions import PassengerAlreadyExistsError, PassengerNotFoundError


class BookingManager:
    def __init__(self):
        self.__airplane = None
        self.__flight = None
        self.__passengers = list()
        self.__reservations = list()
        self.__passenger = None


    @property
    def airplane(self):
        return self.__airplane

    def set_airplane(self, model: str, registration: str, capacity: int):
        self.__airplane = Airplane(model, registration, capacity)

    @property
    def passeger(self):
        return self.__passenger


    @property
    def passengers(self):
        return self.__passengers

    def add_passenger(self, name, email, passport_number, reservations=None, frequent_flyer_points=0):
        self.__passenger = Passenger(name, email, passport_number, reservations, frequent_flyer_points)
        """check if the passenger is already in the DB """
        passengers_in_DB = PassengerActions(passport_number)
        if self.__passenger not in passengers_in_DB.select_passenger():
            self.__passengers.append(self.__passenger)
            passengers_in_DB.insert_passenger()
        else:
            raise PassengerAlreadyExistsError

    def remove_passenger(self, passport_number):
        """check if the passenger is already in the DB """
        passengers_in_DB = PassengerActions(passport_number)
        if self.__passenger in passengers_in_DB.select_passenger():
            self.__passengers.remove(self.__passenger)
            passengers_in_DB.delete_passenger()
        else:
            raise PassengerNotFoundError

    def update_passenger(self, name, email, passport_number, reservations=None, frequent_flyer_points=0):
        """check if the passenger is already in the DB """
        passengers_in_DB = PassengerActions(passport_number)
        if self.__passenger in passengers_in_DB.select_passenger():
            #todo: update the MySQL DB table with an insert
            pass
        else:
            raise PassengerAlreadyExistsError
        
    def get_passenger(self, passport_number):
        """check if the passenger is already in the DB """
        passengers_in_DB = PassengerActions(passport_number)
        if self.__passenger in passengers_in_DB.select_passenger():
            print("Found it!")
        else:
            print(f"The passenger with the {passport_number} was not found!")
            # todo: correct this error
            # raise PassengerNotFoundError

    @property
    def reservation(self):
        return self.__reservations

    def set_reservation(self):
        """reservation = Reservation(reservation_id, passenger, flight, seat_number,status, booking_time)"""
        pass

    @property
    def flight(self):
        return self.__flight
    
    
if __name__=="__main__":
    test = BookingManager()
    # test.add_passenger(name="Gábor", email="gabor@gmail.com", passport_number="B123456",
    #                    reservations=None, frequent_flyer_points=0)
    test.get_passenger(passport_number='12345678')
    test.get_passenger(passport_number='A12345678')

    
    