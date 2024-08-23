# f 문자열 포매팅

name = '홍길동'
age = 18
print(f'나의 이름은{name}입니다. 나이는 {age}살 입니다.')

# f 포매팅은 {}안에 표현식(수식)도 사용 가능하다.

print(f'나의 이름은{name}입니다. 나이는 {age + 10}살 입니다.')

# 정렬

print(f'{'hi':<10}') # 왼쪽 정렬
print(f'{'hi':>10}') # 오른쪽 정렬
print(f'{'hi':^10}') # 가운데 정렬

print(f'{'hi':*^10}') # 채우기

# 실수로 표현

y = 3.42134234

print(f'{y:0.4f}') 
print(f'{y:.4f}') 

print(f'{y:10.4f}') 
print(f'{y:<10.4f}') 
print(f'{y:*<10.4f}') 

# {} 출력
print(f'{{ and }}')
