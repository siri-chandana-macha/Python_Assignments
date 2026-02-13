import logging

logging.basicConfig(
    filename="ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:

    base_fare =200

    def __init__(self, passenger_name, ticket_id, distance):
        self.passenger_name = passenger_name
        self.ticket_id = ticket_id
        self.distance = distance
        self.status = "Booked"

    def calculate_fare(self):
        price = Ticket.base_fare + (self.distance * 2)
        logging.info("price of Ticket %s: %s", self.ticket_id, price)
        return price
        

    def book_ticket(self):
        self.status = "Booked"
        logging.info("Ticket %s booked for %s", self.ticket_id, self.passenger_name)

    def cancel_ticket(self):
        self.status = "Cancelled"
        logging.warning("Ticket %s cancelled", self.ticket_id)

    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        logging.info("Base fare updated to %s", new_fare)



t1 = Ticket("Siri", 101, 300)
t1.book_ticket()
print("Fare:", t1.calculate_fare())
t1.cancel_ticket()

Ticket.update_base_fare(600)
