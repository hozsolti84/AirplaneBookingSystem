from abc import ABC

from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from models.flight import Flight
    from models.reservation import Reservation


from datetime import datetime


class Person(ABC):
    """ Abstract class for all people in the system. """
    def __init__(self, name: str, email:str):
        self.__name = name
        self.__email = email

class Passenger(Person):
    """Represents someone booking flights."""
    def __init__(self,
                 name: str,
                 email: str,
                 passport_number: str,
                 reservations: Optional[List] = None,
                 frequent_flyer_points: int = 0
                 ):
        super().__init__(name, email)
        self.__passport_number = passport_number
        self.__reservations = reservations if reservations is not None else []
        self.__frequent_flyer_points = frequent_flyer_points

    @property
    def passport_number(self):
        return self.__passport_number

    def set_passport_numer(self, passport_number):
        self.__passport_number = passport_number

    @property
    def reservations(self):
        return self.__reservations

    def book_flight(self, flight: "Reservation", seat_number: str) -> Reservation:
        # todo: Reservation(reservation_id, passenger, flight, seat_number,status, booking_time)
        reservation = Reservation(flight, seat_number)
        if reservation not in self.__reservations:
            # todo: implement Passenger.book_flight
            self.__reservations.append(reservation)
        else:
            # todo: Raise reservations error
            pass
        return Reservation

    def cancel_reservation(self, reservation_id: str):
        # todo: implement Passenger.
        pass

    @property
    def frequent_flyer_points(self):
        return self.__frequent_flyer_points

class Employee(Person):
    """Represents airline staff, such as pilots or gate agents."""
    # todo: is the Employee class used somewhere, if not delete it?
    def __init__(self, employee_id: str, role: str):
        self.employee_id = employee_id
        self.role = role
        super().__init__()



