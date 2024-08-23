# 문자열 관련 함수들

# 1. 문자 갯수 세기 - count

a = 'hobby'
print(a.count('b'))

cnt = a.count('b')
print(cnt)

# 2. 문자 위치 찾기 - find

a = 'python is the best choice'
print(a.find('b'))

# 찾는 문자의 제일 처음 나오는 위치를 반환한다

pos = a.find('b')
print(pos)

# 찾는 문자가 없으면, -1을 반환한다

pos = a.find('z')
print(pos)

# 3. 문자 찾기 - index

# 찾는 문자의 제일 처음 나오는 위치를 반환한다

a = 'Life is too short'
pos = a.index('t')
print(pos)

# 만약에, 찾는 문자가 없다면, error가 발생한다

a = 'Life is too short'
# pos = a.index('z')
# print(pos)

# 4. 문자열 삽입하기 - join

a = ',' .join('abcd')
print(a)

# 5. 소문자를 대문자로 바꾸기 - upper

a = 'hi'
print(a.upper())

# 대문자를 소문자로 바꾸기 - lower

a = 'HI'
print(a.lower())

# 7. a문자열에 왼쪽, 오른쪽 공백 지우기

a = '    hi    '
print(a.strip()) # 왼쪽과 오른쪽 공백 지우기
print(a.lstrip()) # 왼쪽 공백 지우기
print(a.rstrip()) # 오른쪽 공백 지우기

# 8. 문자열을 바꾸기 - replace

a = 'Life is too short' 
result = a.replace('Life','your leg')
print(result)

# 9. 문자열 나누기

a = 'Life is too short' 
result = a.split(' ')
print(result)

a = 'a:b:c:d'
result = a.split(':')
print(result)

# 문자열 메서드(함수)를 실행하면,
# 본래의 문자열은 그대로 두고(변하지 않는다),
# 새로운 문자열을 반환한다.

a = 'hi'
result = a.upper()
print(a)
print(result)