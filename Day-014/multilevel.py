# Demonstrate multilevel inheritance

class Person:

    def show_person(self):
        print("I am a Person")


class Employee(Person):

    def show_employee(self):
        print("I am an Employee")


class Manager(Employee):

    def show_manager(self):
        print("I am a Manager")


manager = Manager()

manager.show_person()
manager.show_employee()
manager.show_manager()
