# Assignment-9: OOPS Concepts

# 1. Class Demo and display method
class Demo:
    def display(self):
        print("Hello from Demo class")

obj = Demo()
obj.display()


# 2. Parameterized constructor
class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s = Student1("Soumya", 22)
s.display()


# 3. Constructor overloading using default arguments
class Student2:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student2()
s2 = Student2("Rahul", 21)
s1.display()
s2.display()


# 4. Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

for animal in (Dog(), Cat()):
    animal.sound()


# 5. Single inheritance
class Parent1:
    def show(self):
        print("Parent class")

class Child1(Parent1):
    pass

c1 = Child1()
c1.show()


# 6. Method overriding
class Parent2:
    def show(self):
        print("Parent method")

class Child2(Parent2):
    def show(self):
        print("Child method")

c2 = Child2()
c2.show()


# 7. Multiple inheritance
class Father:
    def skill1(self):
        print("Father skill")

class Mother:
    def skill2(self):
        print("Mother skill")

class Child3(Father, Mother):
    pass

c3 = Child3()
c3.skill1()
c3.skill2()


# 8. Class variable and instance variable
class Student3:
    college = "TAC"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s3 = Student3("Soumya")
s4 = Student3("Rahul")

print(s3.name, s3.college)
print(s4.name, s4.college)