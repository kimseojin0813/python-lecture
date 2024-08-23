# 딕션너리 관련 함수

# 1. 딕션너리에서 key 값 리스트 만들기 : keys() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

result = a.keys() # dict_keys(['name', 'phone', 'birth'])
print(result)

result = list(result) # 리스트로 변경
print(result)

# 2. 딕션너리에서 value 값 리스트 만들기 : values() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

result = a.values() # dict_values(['Pey', '010-0000-1234', '1113'])
print(result)

result = list(result)
print(result)

# 3. 딕션너리에서 key, value 쌍 얻기 : items() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

result = a.items() # dict_items([('name', 'Pey'), ('phone', '010-0000-1234'), ('birth', '1113')])

result = list(result)
print(result)

# 4. 딕션너리의 속성들을 모두 지우기 : clear() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

a.clear()
print(a)

# 5. key로 value 얻기 : get() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

print(a.get('name')) # print(a.['nmae']) 과 동일
print(a.get('phone'))

# 차이: 없는 키를 줬을 때

# print(a['age']) # error  발생
print(a.get('age')) # 딕션너리에 없는 key를 줄 때, None이 반환

# 6. 딕션너리에 해당 key가 있는지 검사 : in() 함수

a = {
    'name' : 'Pey',
    'phone' : '010-0000-1234',
    'birth': '1113'
}

print('nmae' in a) # True
print('email' in a) # False


















