# 딕션너리의 정의 

dic ={
    'name': "pey", # 속성(property)
    'phone': '010-0000-1234', 
    'birth' : '1113'
}

# 위릐 dic 변수에는 3개의 속성값을 가진 딕션너리를 할당

a = {
    1: 'hi'
    }

a = {
    'a': [1, 2, 3]
}
 
# 딕션너리에 속성을 추가하고 삭제하기

# 1. 속성 추가하기

a = {
    'first name': 'John',
    'last name': 'Doe'
}

a['age'] = 17 # 새로운 속성을 추가
print(a)

a['age'] = 20 # 기존의 속성 변경
print(a)

# 2. 요소를 삭제하기

a = {
    'first name': 'John',
    'last name': 'Doe',
    'age' : 17,
    'eyecolor': 'blue'
}

del a['age']
print(a)

a.pop('eyecolor')
print(a)

# 딕션너리의 사용

person = {"김연아": "피겨스케이팅",
          "류현진": "야구",
          "손흥민": "축구",
          "귀도": "파이썬"
 }

# 딕션너리에서 key를 이용해서 value를 얻기

grade = {'pey': 10,
         'julliet': 99
}

print(grade['pey'])
print(grade['julliet'])

a = {
    1: 'a',
    2: 'b'
}

print(a[1])
print(a[2])

dic ={
    'name' : ' pey',
    'phone' : '010-0000-1234',
    'birth' : '1113'
}

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕션너리의  key값은 고유해야 된다. (중복이 없다)

a = {
    1:'a',
    2:'b'
}

# key값이 중복될 경우, 맨 마지막에 선언한 속성값만 남는다

print(a)

# 딕션너리의  key값으로 리스트는 사용 불가
# mutable(변경가능한)한 값은 key로 사용할수 없다

# a = {
#     [1, 2] : 'hi'
# }















































