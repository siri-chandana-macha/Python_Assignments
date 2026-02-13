import logging

logging.basicConfig(
    filename="hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HostelRoom:

    room_rent=6000   

    def __init__(self, room_no, student_name):
        self.room_no=room_no
        self.student_name=student_name
        self.occupied=False

    def allocate_room(self):
        self.occupied=True
        logging.info("Room %s allocated to %s", self.room_no, self.student_name)

    def vacate_room(self):
        self.occupied=False
        logging.warning("Room %s vacated by %s", self.room_no, self.student_name)

    def calculate_monthly_fee(self):
        logging.info("Monthly fee for Room %s is %s", self.room_no, HostelRoom.room_rent)
        return HostelRoom.room_rent

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        logging.info("Room rent updated to %s", new_rent)


r1 = HostelRoom(201, "Siri")
r1.allocate_room()
r1.calculate_monthly_fee()
r1.vacate_room()

HostelRoom.update_room_rent(15000)
