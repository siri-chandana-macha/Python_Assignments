import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Library:
    fine = 20

    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name
        self.is_issued = False

    def issue_book(self):
        if self.is_issued:
            logging.warning(f"{self.book_name} already issued.")
        else:
            self.is_issued = True
            logging.info(f"{self.book_name} issued successfully.")

    def calculate_fine(self, days_used):
        allowed_days = 10
        late_days = max(0, days_used - allowed_days)
        return late_days * Library.fine

    def return_book(self, days_used):
        if self.is_issued:
            fine_amount = self.calculate_fine(days_used)
            logging.info(f"{self.book_name} returned.")
            logging.info(f"Fine: {fine_amount}")
            self.is_issued = False
        else:
            logging.warning(f"{self.book_name} was not issued.")

b1 = Library(101, "Python")
b1.issue_book()
b1.return_book(5)   # No fine

b2 = Library(102, "Java")
b2.issue_book()
b2.return_book(12)  # Fine: 2 × 20 = 40
