
marks = [90, 25, 67, 45, 80]

for i in range(len(marks)):
    if marks[i]>60:
        print(i+1,"번 학생은 합격입니다.")
    else:
        print(i+1,"번 학생은 불합격입니다.")

print()
i=0
while i<len(marks):
    if marks[i]>60:
        print(i+1,"번 학생은 합격입니다.")
    else:
        print(i+1,"번 학생은 불합격입니다.")
    i+=1

    
