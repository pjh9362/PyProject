"""
s, f, i = map(int, input("시작값과 끝값, 수 간격을 입력하세요 : ").split())

tpl = tuple(range(s,f,i))

print(tpl)
"""

inData1 = input("시작 값을 입력하세요 : ")
inData2 = input("끝 값을 입력하세요 : ")
test = input("증가폭을 입력하세요 : ")
print(tuple(range(int(inData1), int(inData2), int(test))))
