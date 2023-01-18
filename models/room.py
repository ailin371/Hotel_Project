from enum import Enum

class RoomType(str, Enum):
    BASIC = 'Basic'
    DELUXE = 'Deluxe'
    SUITE = 'Suite'

class Room(object):
    def __init__(self, id: str, size: float, capacity: int, number_of_beds: int, type: RoomType, price: float):
        self.id = id
        self.size = size
        self.capacity = capacity
        self.number_of_beds = number_of_beds
        self.type = type
        self.price = price
        
    def __str__(self):
        return str(self.__dict__)
