
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
