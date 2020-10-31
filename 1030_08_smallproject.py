
n = int(input("시작하는 정수 입력 : "))
m = int(input("끝나는 정수 입력 : "))

if n>m:
    temp = n
    n=m
    m=temp

sum=0
for i in range(n,m+1):
    sum+=i

print(n, "부터", m, "까지의 합은", sum, "입니다.")


