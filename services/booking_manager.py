from models.airplane import Airplane
from models.person import Passenger, Employee
from models.flight import Flight
from models.reservation import Reservation
class BookingManager:
    def __init__(self):
        # self.airplane1 = Airplane("Airbus A320", "LH123456", 120)
        self.__airplane = None
        self.__passengers= list()
        self.__reservations = list()
        self.__flight = None
        
    @property
    def airplane(self):
        return self.__airplane

    def set_airplane(self, model: str, registration: str, capacity: int):
        self.__airplane = Airplane(model, registration, capacity)

    @property
    def passengers(self):
        return self.__passengers

    def add_passenger(self, name, email, passport_number, reservations, frequent_flyer_points):
        passanger = Passenger(name, email, passport_number, reservations=None, frequent_flyer_points=0)
        if passanger. in
            self.__passengers.append(passanger)
    @property
    def reservations(self):
        return self.__reservations
    @property
    def flight(self):
        return self.__flight