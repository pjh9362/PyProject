
marks = [90, 25, 67, 45, 80]

for i in range(len(marks)):
    if marks[i]<60:
        continue    
    
    print(i+1,"번 학생 축하합니다. 합격입니다.")

print()
i=0
while i<len(marks):
    if marks[i]<60:
        i+=1
        continue
    print(i+1,"번 학생 축하합니다. 합격입니다.")
    i+=1

    
