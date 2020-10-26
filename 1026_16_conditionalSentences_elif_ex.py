fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

season = input("제가 좋아하는 계절은: ")

if season in fruit: #if season in fruit.keys():
    print("정답입니다.", fruit[season])
else:
    print("오답입니다.")

# dictionary 는 keys method를 사용하지 않아도 기본적으로 key를 비교한다


