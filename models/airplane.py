

class Airplane:
    """Defines a specific aircraft model and its seating."""
    def __init__(self, model: str, registration: str, capacity: int):
        """
        :param model: e.g., “Airbus A320”
        :param registration: tail number
        :param capacity:
        :param seat_map: {seat_number: None | Passenger}e.g., {'1A': None, '1B': Passenger(...), ...}
        """
        self.model = model
        self.registration = registration
        self.capacity = capacity

