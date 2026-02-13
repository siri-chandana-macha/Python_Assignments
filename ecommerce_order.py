import logging

logging.basicConfig(
    filename="ecommerce.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Order:

    tax_percentage=10

    def __init__(self, name, address, order_id, price):
        self.name = name
        self.address = address
        self.order_id = order_id
        self.price = price
        self.status = "Placed"
        logging.info("Order is placed by %s", self.name)

    def calculate_total_price(self):
        tax = (self.price * Order.tax_percentage) / 100
        total = self.price + tax
        logging.info("Total price of Order %s", total)
        

    def cancel_order(self):
        self.status = "Cancelled"
        logging.warning("Order %s cancelled", self.order_id)

    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("Tax percentage updated to %s", new_tax)



o1 = Order("Siri", "Hyderabad", 101, 1000)
o1.calculate_total_price()
o1.cancel_order()
Order.update_tax_percentage(20)
