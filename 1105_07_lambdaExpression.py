
def plus_ten(x):
    return x + 10

print(plus_ten(1))


print( lambda x : x + 10)

plus_ten = lambda x : x + 10

print(plus_ten(1))

print((lambda x : x + 10)(1))

#print((lambda x : y = 10; x+y)(1))

y = 10
print((lambda x: x+y)(1))


def plus_ten(x):
    return x+10
print(list(map(plus_ten, [1,2,3])))


print(list(map(lambda x : x + 10, [1,2,3])))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x : str(x) if x % 3 == 0 else x, a)))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(f, a)))



a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y : x*y, a,b)))


def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f,a)))
print(list(filter(lambda x : x > 5 and x < 10, a)))

# reduce

from functools import reduce

def f1(x, y):
    return x+y

a = [1, 2, 3, 4, 5]
print(reduce(f1,a))

print(reduce(lambda x, y : x + y, a))
