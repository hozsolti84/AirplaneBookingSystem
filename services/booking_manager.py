from models.airplane import Airplane
from models.person import Passenger
from models.reservation import Reservation
from repository.passengers_repo import PassengerActions
from exceptions.exceptions import PassengerAlreadyExistsError, PassengerNotFoundError


class BookingManager:
    def __init__(self):
        self.__airplane = None
        self.__flight = None
        self.__passengers = list()       # todo: this should be in the the models.flights, isn't it?
        self.__reservations = list()
        self.__passenger = None
        self.__frequent_flyer_points = None


    @property
    def airplane(self):
        return self.__airplane

    def set_airplane(self, model: str, registration: str, capacity: int):
        self.__airplane = Airplane(model, registration, capacity)

    def get_airplain(self, registration):
        pass

    @property
    def passeger(self):
        return self.__passenger

    @property
    def passengers(self):
        return self.__passengers

    def create_passenger(self, name, email, passport_number, reservations=None, frequent_flyer_points=0):
        passengers_in_DB = PassengerActions(name=name, email=email, passport_number=passport_number,
                                            reservations=reservations, frequent_flyer_points=frequent_flyer_points)
        passenger_data = passengers_in_DB.select_passenger()
        if passport_number not in passenger_data:
            print("The passenger was not found! It will be created!\n")
            """ creating the Passenger obj """
            self.__passenger = Passenger(name, email, passport_number, reservations, frequent_flyer_points)
            # todo: the passenger obj should be added to the Flight obj.
            """ creating the db instance """
            passengers_in_DB.create_passenger('insert')
        else:
            raise PassengerAlreadyExistsError
        """check if the passenger is already in the DB """

    # def update_passenger(self, name, email, passport_number, reservations=None, frequent_flyer_points=0):
    #     passengers_in_DB = PassengerActions(name=name, email=email, passport_number=passport_number,
    #                                         reservations=reservations, frequent_flyer_points=frequent_flyer_points)
    #     if self.__passenger in passengers_in_DB.select_passenger():
    #         pass
    #     else:
    #         raise # todo: which exceptions are needed here?


    def get_passenger(self, passport_number):
        """check if the passenger is already in the DB """
        passengers_in_DB = PassengerActions(passport_number)
        passenger_data = passengers_in_DB.select_passenger()
        if passport_number in passenger_data:
            # 1, 'Zsolt', 'batman@gmail.com', '12345678', 0
            print(f"Customers Number:   {passenger_data[0]}, \n"
                  f"Customers Name:     {passenger_data[1]}, \n"
                  f"Customers Email:    {passenger_data[2]},\n"
                  f"Passpornumber:      {passenger_data[3]}")
            return passenger_data    # todo: ha nem kell töröld az add,remove,update-hez
        else:
            print(f"The passenger with the passport number: {passport_number} was not found!")
            # todo: correct this error
            # raise PassengerNotFoundError

    def delete_passenger(self, passport_number):
        """check if the passenger is already in the DB """
        # TODO: ADD A QUESTION BACK TO THE USER IF THEY REALY WANT TO DO THIS
        passengers_in_DB = PassengerActions(passport_number)
        if self.__passenger in passengers_in_DB.select_passenger():
            self.__passengers.remove(self.__passenger)
            passengers_in_DB.delete_passenger()
        else:
            raise PassengerNotFoundError

    @property
    def reservation(self):
        return self.__reservations

    def set_reservation(self, reservation_id, passenger, flight, seat_number,status, booking_time):
        reservation = Reservation(reservation_id, passenger, flight, seat_number,status, booking_time)
        return reservation

    @property
    def flight(self):
        return self.__flight
#

if __name__=="__main__":
    test = BookingManager()
    # test.create_passenger(name='Róbert Kazsás', email='kasza1984@gmail.com', passport_number='9000000', reservations=None, frequent_flyer_points=0)
    # # test.get_passenger(passport_number='4444')
    # # test.update_passenger(name="Balazs Róbert", email="robert11@gmail.com", passport_number="3333",reservations=None, frequent_flyer_points=200)
    # # test.get_passenger(passport_number='12345678')
    # # test.get_passenger(passport_number='A23456789   ')
    # # test.add_passenger(passport_number='B123456')
    test.airplane("Airbus 100", "A00001", 100)
    test.flight()
    test.passenger()
