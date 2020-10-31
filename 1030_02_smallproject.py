
a = 150
g = 30

buy_a, buy_g = map(int,input().split())

sum=0

if buy_a >= 10:
    sum=int((a*0.9)*buy_a) + g*buy_g
else:
    sum=a*buy_a + g* buy_g

print("총액 : ", sum)
