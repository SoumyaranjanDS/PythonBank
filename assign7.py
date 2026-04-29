

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
