
inFp, outFp = None, None
inStr = ""
inFp = open("data2.txt", "r", encoding = "utf-8")
outFp = open("data2_copy.txt", "w", encoding = "utf-8")

inList = inFp.readlines()

for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("------ 정상적으로 파일이 복사되었음 -----")
