# Create a class named Person, with firstname and lastname properties, and a print name method

class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        print(f"{self.firstname} {self.lastname}")

Person("Anil","Mula").name()
