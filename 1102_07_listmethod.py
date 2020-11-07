a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

print("\n*********************\n")

for i in [38, 21, 53, 62, 19]:
    print(i)

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

print()

for index, value in enumerate(a):
    print(index+1, value)

print()

for index, value in enumerate(a, start = 1):
    print(index, value)
