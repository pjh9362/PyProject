
# replace
print("Hello, world!".replace("world", "Python"))

s = "Hello, world!"
s.replace("world!", 'Python')
print(s)

# traunslate

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))


# split

print("apple pear grampe pineapple orange".split())

print("apple, pear, grape, pineapple, orange".split(", "))

# join

print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print(' and '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print(''.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# upper

print('python'.upper())
print(''.join(['apple', 'pear', 'grape', 'pineapple', 'orange']).upper())

# lower
print('PYTHON'.lower())
print("Hello World!".lower())
print("My BirthDay is Dec 26".lower())

# strip - lstrip() and rstrip() and stip()

print('        Python        '.lstrip())
print('        Python        '.rstrip())
print('        Python        '.strip())

# strip('삭제할문자들')
print(',.,.,.,.,..,.,p,.,.,y.,t,..h,.o.n.,..,.,.,.,.'.lstrip(',.'))

print(',.,.,.,.,..,.,p,.,.,y.,t,..h,.o.n.,..,.,.,.,.'.rstrip(',.'))

print(',.,.,.,.,..,.,p,.,.,y.,t,..h,.o.n.,..,.,.,.,.'.strip(',.'))
print(', python.'.strip(',.'))


# ljust() rjust() center()

print('python'.ljust(10))

print('python'.rjust(10))

# print('python'.ljust(10, fillchar='!',/))

print('python'.center(10))
print('python'.center(11)) #공백이 왼쪽에 더 많이 들어간다


# method chaining

print('python'.rjust(10).upper())


# zfill(length)

print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

# find('찾을문자열') retrun index or -1(못찾은경우)

print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))

# rfind('찾을문자열')

print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))

# count('문자열')

print('apple pineapple'.count('pl'))
print('apple pineapple'.count('xx'))


