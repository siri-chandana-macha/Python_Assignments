import logging

logging.basicConfig(
    filename="recharge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Recharge:

    recharge_plan=200   

    def __init__(self, mobile_no):
        self.mobile_no=mobile_no
        self.balance=0
        self.validity=0

    def do_recharge(self, amount):

        if amount <= 0:
            logging.error("Invalid recharge amount for %s", self.mobile_no)

        if amount < Recharge.recharge_plan:
            logging.warning("Recharge amount less than plan for %s", self.mobile_no)
            logging.info("Recharge amount should be minimum", Recharge.recharge_plan)
            
        if self.validity > 0:
            logging.warning("Recharge not required. Plan already active")

        self.balance +=amount
        self.validity=30
        logging.info("Recharge done for %s of amount %s", self.mobile_no, amount)

    def check_validity(self):
        if self.validity == 0:
            print("No active plan")
        else:
            logging.info("Validity for %s is %s days", self.mobile_no, self.validity)
        

    def show_balance(self):
        logging.info("Balance for %s is %s", self.mobile_no, self.balance)
        

    @classmethod
    def update_recharge_plans(cls, new_plan):
        cls.recharge_plan = new_plan
        logging.info("Recharge plan updated to %s", new_plan)


r1 = Recharge("9988776655")
r1.do_recharge(200)
r1.show_balance()
r1.check_validity()

Recharge.update_recharge_plans(599)
