

class BookingExceptionsError(Exception):
	def __init__(self, message=f"Booking Error"):
		self.message = message
		super().__init__(message)

class SeatAlreadyBookedError(BookingExceptionsError):
	def __init__(self, message=f"The seat is already booked, by another customer!"):
		self.message = message
		super().__init__(message)

class SeatDoesNotExistError(BookingExceptionsError):
	def __init__(self, message=f"The seat does not exists!"):
		self.message = message
		super().__init__(message)

class OverlappingFlightError(BookingExceptionsError):
	def __init__(self, message=f"The customer has another flight booked already!"):
		self.message = message
		super().__init__(message)

class BookingValidationError(BookingExceptionsError):
    """
	reservation request violates business rules or contains invalid data
    it's about application-level logic being incorrect.
    e.g.    1. Invalid seat number format or seat not on airplane

    """
    def __init__(self, message="Invalid data type in the booking process!"):
		self.message = message
		super().__init__(message)
class FlightTimeError(BookingExceptionsError):
    def __init__(self, departure_time, arrival_time):
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        if arrival_time <= departure_time:
            message = f"Invalid flight times: arrival_time ({arrival_time}) must be after departure_time ({departure_time})"
        else:
            message = "Valid flight time error, but was still raised."  # Should never really happen
        super().__init__(message)

class PassengerNotFoundError(BookingExceptionsError):
	def __init__(self, message=""):
		self.message = message
		super().__init__(message)

class PassengerAlreadyExistsError(BookingExceptionsError):
	def __init__(self, message="The passanger already exists!"):
		self.message = message
		super().__init__(message)
