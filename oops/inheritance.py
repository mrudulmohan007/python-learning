# parent class
class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name, self.contact)


# child class
class Doctor(Person):
    pass


class Patient(Person):
    pass
doc1=Doctor("Mrudul",123456)
pat1=Patient("stuart",56789)
doc1.address()
pat1.address()