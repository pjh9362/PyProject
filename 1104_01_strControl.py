
s = 'apple pineapple apple pineapple'
target = 'pl'

index = []

for i in range(len(s)-len(target)):
    if s[i:i+len(target)] == target:
        index.append(i)

print(index)

##############################################

s = 'apple pineapple apple pineapple'
target = 'pl'

index = []

cutting = 0
cpy = s

while cpy.find(target) != -1:
    temp = cpy.find(target)
    index.append(cutting+temp)
    cutting += temp+len(target)
    cpy=cpy[temp+len(target):]

print(index)


#############################################

s = 'apple pineapple'

find1 = s.find('pl')
print(find1)

newFind = find1 + 2
s = s[newFind:]

find2 = s.find('pl')
find2 = newFind + find2
print(find2)


##############################################
s1 = 'apple pineapple apple pineapple'
s2 = 'pl'

cnt = s1.find(s2)

print(cnt)

while s1[cnt+1:].find(s2) != -1:
    cnt = s1[cnt+1:].find(s2) + cnt + 1
    print(cnt)

############################################

cnt = -1
while s1[cnt+1:].find(s2) != -1:
    cnt = s1[cnt+1:].find(s2) + cnt + 1
    print(cnt)

print()

cnt = -1
while s1[cnt+1:].find(s2) != -1:
    cnt = s1[cnt+1:].find(s2) + cnt + 1
    print(cnt)


##################################################

import re
str1 = 'apple pineapple apple pineapple'
str2 = 'pl'

for a in re.finditer(str2, str1):
    print(a.start(), a.end())

