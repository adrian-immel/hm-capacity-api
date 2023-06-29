from dataclasses import dataclass
from typing import Optional
import parser


@dataclass
class location:
    name: str
    lrz_subdistrict_id: str
    specific_access_points: Optional[list] = None
    clients: float = 0
    capacity_level_in_percent: float = None
    timestamp: int = None

    def __post_init__(self):
        parser.get_location_data(self)

    def update_clients(self, clients_to_add: float):
        if clients_to_add is not None:
            self.clients = self.clients + clients_to_add
