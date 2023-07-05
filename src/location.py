from dataclasses import dataclass
from typing import Optional
import parser


"""
This class is used to store the data of a location.
"""
@dataclass
class location:
    name: str
    lrz_subdistrict_id: str
    static_max_clients: int = None
    specific_access_points: Optional[list] = None
    clients: int = 0
    capacity_level_in_percent: float = None
    timestamp: int = None

    def __post_init__(self):
        parser.get_location_data(self)
        self.capacity_level_in_percent = parser.percentage_calculator(self)

    """
    This method is used to update the clients of a location.
    :param clients_to_add: the amount of clients to add to the current amount of clients
    """
    def update_clients(self, clients_to_add: int):
        if clients_to_add is not None:
            self.clients = round(self.clients + clients_to_add)
