class Hospital:
    hospital_name="Apollo Hospital"
    consultation_fee=500
    room_charge=1000

    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
        self.admitted=False

    def admit_patient(self):
        self.admitted=True
        print(self.name,"is admitted")

    def discharge_patient(self):
        if self.admitted:
            self.admitted=False
            print(self.name,"is discharged")
        else:
            print(self.name,"is not admitted")


    def calculate_bill(self,days_admitted):
        if self.admitted:
            total=(Hospital.room_charge * days_admitted)+ Hospital.consultation_fee
            print("Total Bill:",total)
        else:
            total=Hospital.consultation_fee
            print("Total bill:",total)


    @classmethod
    def update_consultation_fee(cls,new_consultation_fee):
        cls.consulation_fee=new_consultation_fee
        print("updated consulation fee",new_consultation_fee)

h1=Hospital("kavya",19,"malaria")
h1.admit_patient()
h1.calculate_bill(5)
h1.discharge_patient()

h2=Hospital("veer",55,"tootache")
h2.discharge_patient()
h2.calculate_bill(0)





        
