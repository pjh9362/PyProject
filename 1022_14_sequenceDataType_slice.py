'''
b = tuple(range(0,100, 10))

b[2:5] = ('a', 'b', 'c')

TypeError: 'tuple' object does not support item assignment


r = range(10)

r[2:5] = range(0, 3)

TypeError: 'range' object does not support item assignment


hello = 'Hello, world!'

hello[7:13] = 'Python'

TypeError: 'str' object does not support item assignment


'''

