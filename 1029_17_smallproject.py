cost = int(input())
cpn = input()

if cpn == "Cash3000":
    print(cost-3000)
elif cpn == "Cash5000":
    print(cost-5000)
else:
    print("쿠폰이 적용되지 않았습니다.")
    print(cost)
