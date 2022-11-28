# French 11.28.22

names = []

for x in range(10):
    acceptedName = input("Enter name: ")
    names.append(acceptedName)

print(names)

for x in range(10):
    print(names[0])
    names.pop(0)

print(names)
