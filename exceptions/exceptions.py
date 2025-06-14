#######################################
#				 EXPETIONS 			  #
#######################################
""""""
"""		Utility Expetions 			"""
class UtilityException(Exception):
	def __init__(self, message="There was a problem with the called utility function"):
		super().__init__(message)

class GetdataExceptionError(UtilityException):
	def __init__(self, message="The utility function get_data has run in to a problem!"):
		super().__init__(message)

"""		Config Exceptions			"""
class ConfigException(Exception):
	def __init__(self, message="There is a problem with the configuration"):
		super().__init__(message)
		self.message = message


class SectionNotFound(ConfigException):
	def __init__(self, message="The section was not found"):
		super().__init__(message)
		self.message=message

class KeyNotFoundInConfig(ConfigException):
	def __init__(self, message="The key was not found"):
		super().__init__(message)
		self.message=message

class ValueNotFoundInConfig(ConfigException):
	def __init__(self, message="The value was not found"):
		super().__init__(message)
		self.message=message


"""		Booking Exceptions			"""

class BookingExceptionsError(Exception):
	def __init__(self, message=f"Booking Error"):
		super().__init__(message)
		self.message = message


class SeatAlreadyBookedError(BookingExceptionsError):
	def __init__(self, message=f"The seat is already booked, by another customer!"):
		super().__init__(message)
		self.message = message


class SeatDoesNotExistError(BookingExceptionsError):
	def __init__(self, message=f"The seat does not exists!"):
		super().__init__(message)
		self.message = message


class OverlappingFlightError(BookingExceptionsError):
	def __init__(self, message=f"The customer has another flight booked already!"):
		super().__init__(message)
		self.message = message


class BookingValidationError(BookingExceptionsError):
	"""
	reservation request violates business rules or contains invalid data
    it's about application-level logic being incorrect.
    e.g.    1. Invalid seat number format or seat not on airplane

    """
	def __init__(self, message="Invalid data type in the booking process!"):
		super().__init__(message)
		self.message = message

class FlightTimeError(BookingExceptionsError):
	def __init__(self, message, departure_time, arrival_time):
		super().__init__(message)
		self.departure_time = departure_time
		self.arrival_time = arrival_time
		if arrival_time <= departure_time:
			self.message = f"Invalid flight times: arrival_time ({arrival_time}) must be after departure_time ({departure_time})"
		else:
			self.message = "Valid flight time error, but was still raised."  # Should never really happen


class PassengerExeptionError(Exception):
	def __init__(self, message="The passenger was not found in the DB!"):
		self.message = message
		super().__init__(message)


class PassengerNotFoundError(PassengerExeptionError):
	def __init__(self, message="The passenger was not found!"):
		# self.message = message
		super().__init__(message)


class PassengerAlreadyExistsError(PassengerExeptionError):
	def __init__(self, message="The passanger already exists!"):
		# self.message = message
		super().__init__(message)

