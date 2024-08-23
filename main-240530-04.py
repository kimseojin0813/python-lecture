# format 함수를 이용한 포매팅

print('I eat {0} apples. So I was sick for {1} days.'. format(10, 'three'))
print('I eat {} apples. So I was sick for {} days.'. format(10, 'three'))
print('I eat {1} apples. So I was sick for {0} days.'. format(10, 'three'))

number = 10
day = 'three'
print('I eat {0} apples. So I was sick for {1} days.'. format(number, day))

# 이름으로 넣기

print('I eat {number} apples. So I was sick for {day} days.'. format(number = 10, day = 'three'))

# 정렬하기

print('{0:<10}' .format('hi')) # 왼쪽 정렬
print('{0:>10}' .format('hi')) # 오른쪽 정렬
print('{0:^10}' .format('hi')) # 가운대 정렬

# 공백 채우기 

print('{0:*^10}' .format('hi')) 
print('{0:*<10}' .format('hi')) 
print('{0:*>10}' .format('hi')) 

# 소수점 표현하기

y = 3.42134234
print('{0:0.4f}' .format(y))
print('{0:.4f}' .format(y))

# 정렬

print('{0:10.4f}' .format(y))
print('{0:>10.4f}' .format(y))
print('{0:<10.4f}' .format(y))

#공백 채우기

print('{0:*<10.4f}' .format(y))

# {} 표시하기

print('{{}}' .format())

