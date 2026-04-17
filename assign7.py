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