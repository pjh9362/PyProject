
# 몇 줄이나 있는지 모를때 사용가능

inFp = None
inStr = ""
inFp = open("data1.txt", "r", encoding = "utf-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")

inFp.close()


# 한 번에 모두 읽어들이기 - readlines() 함수는 파일의 내용을 통으로 리스트에 저장

inFp = open("data1.txt", "r", encoding = "utf-8")

inList = []
inList = inFp.readlines()
print(inList)

for inStr in inList:
    print(inStr, end = '')

inFp.close()

