"""In the program get a line entered by the user from the keyboard.
Use the loop to split the string into characters (single letters) and add each single letter as a new element of the list."""

a = input("Enter something: ")

count = 0
for i in a:
    if i != 0:
        count += 1
# print(count)

# print(a[0])

b = []
for i in range(count):
    b.append(a[i])
    i += 1
print(b)
