x = {}
print(x)

y = dict()
print(y)

#dict()
lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1)

#zip() 활용 zip안에는 list tuple 모두 가능
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

# list안에 (key, value) 나열
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

#dict() 안에 중괄호로 dictinary를 생성
lux4 = dict({'health' : 490, 'mana' : 334, 'melee':550, 'armor':18.72})
print(lux4)

lux = {'health' : 490, 'mana' : 334, 'melee':550, 'armor' : 18.72}
print(lux['health'])
print(lux['armor'])

lux['health'] = 2037
lux['mana'] = 1184
print(lux)

lux['mana_regen'] = 3.28
print(lux)

# 없는 key 를 호출하면 에러 발생
# print(lux['attack_speed'])

print('health' in lux)

print('attack_speed' in lux)

print('attack_speed' not in lux)
print('health' not in lux)

print(lux)
print(len(lux))
