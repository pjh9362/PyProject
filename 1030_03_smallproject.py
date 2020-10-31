cost_a = 150
cost_b = 30

a = int(input("사과:"))
b = int(input("귤:"))

sum=cost_a * a + cost_b*b
if a>=5 and b>=3:
    sum=int(sum*0.7)

print("총액 : ",sum)

