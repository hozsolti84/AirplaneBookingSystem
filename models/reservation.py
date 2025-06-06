from datetime import datetime

from models.flight import Flight
from models.person import Passenger

class Reservation:
    def __init__(self, reservation_id: str, passenger: "Passenger obj", flight: "Flight obj", seat_number: str,
                 status: str, booking_time: datetime):
        self.__reservation_id = reservation_id
        self.__passenger = passenger
        self.__flight = flight
        self.__seat_number = seat_number
        self.__status = status                 #  "confirmed", "cancelled"
        self.__booking_time = booking_time


    # todo:     @property-s: __flight, __seat_number, __status, __booking_time????

    def create_reservation(self):
        pass

    def update_reservation(self):
        pass

    def cancel_reservation(self):
        """updates status, removes from passenger and flight records"""
        pass

    def summary(self):
        """returns printable reservation details"""
        return (f"reservation_id: {self.__reservation_id},\n"
                f"passenger: {self.__passenger.name},\n " 
                f"passenger: {self.__passenger.passport_number},\n "
                f"flight: {self.__flight},\n "
                f"seat_number: {self.__seat_number}, \n "
                f"status: {self.__status}"
                f"booking_time: {self.__booking_time}")

