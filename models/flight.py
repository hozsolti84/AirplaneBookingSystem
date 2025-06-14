from __future__ import annotations
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from models.airplane import Airplane
    from models.reservation import Reservation
    from models.person import Passenger
from datetime import datetime

class Flight:
    """
    Represents a scheduled trip using a specific airplane.
    • Rules:
    ○ Cannot double-book a seat
    ○ arrival_time must be after departure_time
    """
    def __init__(self, flight_number: str, origin: str, destination: str,
                 departure_time: datetime, arrival_time: datetime, airplane: Airplane, reservations: List[Reservation]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.airplane = airplane
        self.reservations = reservations if reservations is not None else []

    def is_seat_available(self, seat_number: str) -> bool:
        pass

    def assign_seat(self, passenger: Passenger, seat_number: str) -> Reservation:
        pass

    def cancel_seat(self, reservation_id: str):
        pass

    def get_available_seats(self) -> list[str]:
        pass


