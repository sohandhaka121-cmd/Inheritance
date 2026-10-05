class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(Person):
    School_name = "Govt School"

    def __init__(self, name, age, roll, marks=0):
        super().__init__(name, age)
        self.roll = roll
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks, marks must be between 0 to 100")

    def get_marks(self):
        return self.__marks


s1 = Student("Sohan", 18, 10, 80)
s2 = Student("WAZID", 14, 16, 70)

s1.show_info()
print(s1.roll)
print(s1.get_marks())
s2.show_info()
print(s2.roll)
print(s2.get_marks())