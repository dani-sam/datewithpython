# create sample of class and init method

class Dog:

    def __init__(self, name , age):
        self.name = name
        self.age = age
        

    def getName(self):
        return self.name
    def getAge(self):
        return self.age


# d = Dog("Tim",32)
# print(d.getAge())
# d2 = Dog("Bill",41)
# print(d2.getName())


# creating multiple class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
            return self.grade    
        
    

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)


# s1 = Student("tim",19,93)
# s2 = Student("Bill",19,72)
# s3 = Student("mia",19,89)


# course = Course("science",2)
# course.add_student(s1)
# course.add_student(s3)
# print(course.get_average_grade())     


# inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} color")
    
    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("bark")


# p = Pet("tim",31)
# p.speak()    
# c = Cat("tom",4,"white")
# c.show()
# d = Dog("jack",9)
# d.speak() 

# class attribute

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.addPerson()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def addPerson(cls):
        cls.number_of_people += 1
    

# p1 = Person("joe")
# p2 = Person("tim")
# p3 = Person("tony")
# print(Person.number_of_people_())


# static method

class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
# m = Math()
# print(m.add5(55))