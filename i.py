class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(People):
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


s1 = Student("Mahi", 18, 10, 38)
s2 = Student("risat", 13, 10, 72)
s3 = Student("Sohanur", 18, 19, 88)



s1.show_info()
print(s1.roll)
print(s1.get_marks())
s2.show_info()
print(s2.roll)
print(s2.get_marks())
s3.show_info()
print(s3.roll)
print(s3.get_marks())
