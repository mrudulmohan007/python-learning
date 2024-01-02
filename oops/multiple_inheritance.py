class Mother:
    def mother_talk(self):
        print('Mother talking')
class Father:
    def father_walk(self):
        print('Father walking')


class Child(Father, Mother):  # Multiple Inheritance
    def child_walk(self):
        print('Child walking')


# Usage
child = Child()

child.father_walk()  # Father's method inherited by Child
child.mother_talk()  # Mother's method inherited by Child
child.child_walk()   # Child's own method
