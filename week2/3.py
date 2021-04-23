# Create a class of Jet inventory with two arguments i.e name and country. Also add the minimum 2 items in the class and print them.

class Jet:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def testOutput(self):
        print(f"{self.name} of {self.country}")

Jet("abc", "Danmark").testOutput()
