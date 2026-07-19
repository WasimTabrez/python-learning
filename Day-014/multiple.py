# Demonstrate multiple inheritance

class Father:

    def father_property(self):
        print("Father: Owns a House")


class Mother:

    def mother_property(self):
        print("Mother: Owns Gold")


class Child(Father, Mother):

    def child_property(self):
        print("Child: Owns a Laptop")


child = Child()

child.father_property()
child.mother_property()
child.child_property()
