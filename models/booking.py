from datetime import datetime

class Booking(object):
    def __init__(self, customer_id: int, room_id: int, arrival_date: datetime, departure_date: datetime, total_price: float):
        self.customer_id = customer_id
        self.room_id = room_id
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.total_price = total_price
        
min_booking_times = {
    "Basic": 1,
    "Deluxe": 2,
    "Suite": 3
}
