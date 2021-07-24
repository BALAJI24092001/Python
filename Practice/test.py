class admission:
    def __init__(self):
        self.feePaid = 0
        self.name = None
        self.cgpa = 0.0
        self.gender = None

    def details(self):
        self.name = str(input("Enter students name: "))
        self.cgpa = float(input("Enter 10th class CGPA: "))
        self.gender = str(input("Enter gender of student(small case m/f/o): "))

    def eligibility(self):
        if self.cgpa > 7.0:
            if self.gender == "m":
                self.feePaid = int(input("Pay admission fee(1000): "))
            elif self.gender == "f":
                self.feePaid = int(input("Pay admission fee(500): "))
            elif self.gender == "o":
                self.feePaid = int(input("Pay admission fee(200): "))
            else:
                print("Invalid")
                self.feePaid = -1

    def reciept(self):
        if self.feePaid == 1000 or self.feePaid == 500 or self.feePaid == 200:
            print("Name :  ", "	", "	", self.name)
            print("CGPA :  ", "	", "	", self.cgpa)
            print("Fee paid:", "	", "	", self.feePaid)
            print("Admiossion Status:", "	""Processed",)
        else:
            print("Student admissionn rejeced.")


a = admission()
a.details()
a.eligibility()
a.reciept()
