class Person:
    def print_message(self):
        print("Message from Person")


class Student(Person):
    def print_message(self):
        print("Message from Student")
        # super().print_message()


class Programmer(Person):
    def print_message(self):
        print("Message from Programmer")
        # super().print_message()


class StudentProgrammer(Programmer, Student):
    # def print_message(self):
    #     super().print_message()
    pass


print(StudentProgrammer.__mro__)
jack = StudentProgrammer()
jack.print_message()
