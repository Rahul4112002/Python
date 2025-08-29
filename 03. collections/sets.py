'''Set Examples'''

a = {1, 8, 9, "hello", 2, 3, 4, 5}
print("Iterating over set: ")
for i in a:
    print(i)
    
# Clear set
a = {8, 1, 2, 3, 4}
a.clear()
print("Cleard set", a)

# Set difference
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Difference b - a =", b - a)

# Set union
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Union AUB =", b | a)

# Set intersection
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("Intersection A & B", b & a)