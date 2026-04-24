lst = []
for i in range(10):
    lst.append(int(input("Enter number: ")))

print("List:", lst)

print("First 3 elements:", lst[:3])
print("Last 3 elements:", lst[-3:])
print("Alternate elements from 2nd to 8th position:", lst[1:8:2])
print("Reverse list:", lst[::-1])

x = int(input("Enter value to count: "))
print("Count:", lst.count(x))

print("Concatenation:", lst + lst)
print("Repetition:", lst * 2)

print("Largest:", max(lst))
print("Smallest:", min(lst))

x = int(input("Enter value to remove: "))
if x in lst:
    lst.remove(x)
print("After removing:", lst)

pos = int(input("Enter position to insert: "))
val = int(input("Enter new value: "))
lst.insert(pos, val)
print("After inserting:", lst)

print("Ascending order:", sorted(lst))
print("Descending order:", sorted(lst, reverse=True))

x = int(input("Enter value to search: "))
if x in lst:
    print("Found at position:", lst.index(x))
else:
    print("Not found")





s = input("Enter a string: ")

print("Length:", len(s))
print("Alternate characters:", s[::2])
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())
print("Replace spaces with dash:", s.replace(" ", "-"))
print("Number of 'a':", s.count('a'))
print("Reversed string:", s[::-1])

# 1. Dictionary with user input

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    students[roll] = name

print(students)

roll = int(input("Enter new roll number: "))
name = input("Enter new name: ")
students[roll] = name

print(students)

print(students.keys())
print(students.values())

roll = int(input("Enter roll number to search: "))
print(students.get(roll, "Not found"))

roll = int(input("Enter roll number to delete: "))
students.pop(roll, "Not found")
print(students)

roll = int(input("Enter roll number to update: "))
name = input("Enter updated name: ")
students[roll] = name
print(students)

for r, n in students.items():
    print(r, n)


# 2. Tuple with user input

lst = []

for i in range(6):
    x = int(input("Enter number: "))
    lst.append(x)

t = tuple(lst)

print(t)
print(len(t))
print(max(t), min(t))

print(45 in t)

lst = list(t)
lst[2] = int(input("Enter new 3rd element: "))
t = tuple(lst)
print(t)

lst = list(t)
lst.pop(3)
t = tuple(lst)
print(t)

for x in t:
    print(x, x**3)