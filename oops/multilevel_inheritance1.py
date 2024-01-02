class Grandfather:
    def grand_walk(self):
        print('Grandfather walking')


class Father(Grandfather):
    def father_walk(self):
        print('Father walking')

    def father_talk(self):
        print('Father talking')


class Child(Father):
    def child_walk(self):
        print('Child walking')

    def sing(self):
        print('Child singing')


# Usage
grandfather = Grandfather()
father = Father()
child = Child()

grandfather.grand_walk()
father.grand_walk()  # Grandfather's method inherited by Father
child.grand_walk()   # Grandfather's method inherited by Child
child.father_walk()  # Father's method inherited by Child
child.child_walk()   # Child's own method
