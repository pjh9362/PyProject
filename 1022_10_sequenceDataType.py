a=[38, 21, 53, 62, 19]

print("Before : ", a)

del a[2]

print("After : ", a)


b = (38, 21, 53, 62, 19)
# del b[2] tuple은 del을 지원하지 않음

r = range(0, 10, 2)
# del r[2]

hello = "Hello, world!"
# del hello[2]


