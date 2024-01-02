class Father:
    def father_walk(self):
        print('Father can walk')


class Son(Father):  # Hierarchical Inheritance
    def son_talk(self):
        print('Son talking')


class Daughter(Father):  # Hierarchical Inheritance
    def daughter_sing(self):
        print('Daughter singing')


# Usage
son = Son()
daughter = Daughter()

son.father_walk()  # Father's method inherited by Son
son.son_talk()  # Son's own method
daughter.father_walk()  # Father's method inherited by Daughter
daughter.daughter_sing()  # Daughter's own method
