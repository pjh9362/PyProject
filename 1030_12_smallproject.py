name_list = ['mattew', 'mark', 'luke', 'john', 'paul', 'peter']

target = ['m', 'h']

count = 0

'''
for name in name_list:
    if 'm' in name or 'h' in name:
        count+=1

print("m 또는 h가 이름에 포함된 사람은", count, "명 입니다.")
'''
'''
for name in name_list:
    for i in range(len(name)):
        if name[i]=='m' or name[i]=='h':
            count+=1
            break
'''

for name in name_list:
    for c in name:
        if c=='m' or c == 'h':
            count+=1
            break


print("m 또는 h가 이름에 포함된 사람은", count, "명 입니다.")
    
