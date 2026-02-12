import logging

logging.basicConfig(
    filename="exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Exam:

    pass_marks = 35   

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.is_started = False
        self.is_submitted = False   
        self.score = 0

    
    def start_exam(self):
        self.is_started = True
        logging.info("Exam started for %s", self.student_name)

    def calculate_score(self, marks):
        self.score = marks
        return self.score


    def submit_exam(self, marks):
        if not self.is_started:
            logging.warning("Exam not started for %s", self.student_name)
    
        if self.is_submitted:
            logging.warning("Exam already submitted by %s", self.student_name)
            
        self.calculate_score(marks)
        self.is_submitted = True
        
        if self.score >= Exam.pass_marks:
            logging.info("%s passed with %s marks",self.student_name, self.score)
        else:
            logging.info("%s failed with %s marks",self.student_name, self.score)

    
    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks
        logging.info("Pass marks updated to %s", cls.pass_marks)

s1 = Exam(1, "Ravi")
s1.start_exam()
s1.submit_exam(40)

Exam.update_pass_marks(50)

s2 = Exam(2, "Gita")
s2.start_exam()
s2.submit_exam(45)
