
scores = [86, 72, 98, 60, 45]

grade_counter=[0, 0, 0, 0, 0]

for i in scores:
    if i>=85:
        grade_counter[0]+=1
    elif i>=70:
        grade_counter[1]+=1
    elif i>=55:
        grade_counter[2]+=1
    elif i>=40:
        grade_counter[3]+=1
    else:
        grade_counter[4]+=1

print(grade_counter)
