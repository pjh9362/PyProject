stones = dict( zip([1,2,3,4,5,6,7,8,9,10], [20.5, 13.4, 6.9, 16.3, 9.7, 24.3, 18.2, 5.7, 11.4, 8.3]))

print(stones)

sum=0

for k in stones:
    sum+=stones[k]

avg = sum/len(stones)

print(round(avg,2))



