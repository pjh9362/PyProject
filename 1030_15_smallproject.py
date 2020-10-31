
votes = [2,5,3,4,1,5,1,5,5,3]

candidates = ["", "전정국", "김남준", "박지민", "정호석", "김태형"]
n = len(candidates)

result = [0] * n

for i in votes:
    result[i]+=1

winner_index = 0
for i in range(len(result)):
    if result[winner_index] < result[i]:
        winner_index = i

print(candidates[winner_index], "후보가 총", result[winner_index], "표를 얻어 당선되었습니다.")
