import random

l = []
result = []
for i in range(10):
    while len(l)<7:
        temp = random.randint(1,50)
        if temp not in l:
            l.append(temp)
    l.sort()
    result.append(l)
    l=[]

for t in result:
    print(t)

print("\n**********************\n")

for i in range(10):
    l = []
    l = random.sample(range(1,51), 7)
    l.sort()
    print(l)

print("\n**********************\n")

#reference
for i in range(10):
    lotto_numbers = []
    while len(lotto_numbers) != 7:
        lotto_number = random.randint(1,50)
        if lotto_number not in lotto_numbers:
            lotto_numbers.append(lotto_number)
    #print(lotto_numbers)
    lotto_numbers.sort()
    print(lotto_numbers)

print("\n**********************\n")

for i in range(10):
    l = list(range(1, 51))
    lotto_numbers = []
    for x in range(7):
        r = random.choice(l)
        l.remove(r)
        lotto_numbers.append(r)
    lotto_numbers.sort()
    print(lotto_numbers)



