l = []

for i in range(1,101):
    if i%3==0 or i%5==0 or i%15==0:
        l.append(i)

for i in l:
    print(i)

