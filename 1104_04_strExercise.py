
path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-2\\data.txt'

l = path.split("\\")
print(l)
filename = l[-1]

l.reverse()
print(l[0])

index = path.rfind('\\')
filename = path[index+1:]
print(filename)
