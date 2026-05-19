
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



# Assignment-10

# 1. Employee class
class Employee:
    def __init__(self, empId, name):
        self.empId = empId
        self.name = name

    def show(self):
        print("Employee ID:", self.empId)
        print("Employee Name:", self.name)

e = Employee(101, "Soumya")
e.show()


# 2. Wish class
class Wish:
    def greet(self, name):
        print("Welcome", name)

name = input("Enter your name: ")
w = Wish()
w.greet(name)


# 3. Calculator class
class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

c = Calculator()
c.add(10, 5)
c.subtract(10, 5)


# 4. Create file and write text
file = open("sample.txt", "w")
file.write("This is a sample text file.")
file.close()

print("File created successfully.")


# 5. Fetch data from URL and write in file
import urllib.request

url = "https://example.com"
data = urllib.request.urlopen(url).read()

file = open("url_data.txt", "wb")
file.write(data)
file.close()

print("URL data written successfully.")
