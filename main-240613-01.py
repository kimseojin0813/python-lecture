# 불(bool,bolean) 자료형

# 변수에 할당

a = True
b = False

print(a, type(a))
print(b, type(b))

# 조건식

print(1 == 1)
print(2 < 1)
print(2 > 1)

# 자료형의 참과 거짓

#  값이 있으면, True
# 값이 없으면, False

# bool 연산
print(bool(""))
print(bool(0))
print(bool([1, 2, 3]))

# bool은 while문이나 if문에서 중요하게 사용된다

# list를 복사할때

a = [1, 2, 3]
b = a # 리스트 [1,2,3]이 에 복사X

a[0] = 5

print(b)

# list a 변수를 에 복사하고자 할 때
# 1. [:]를 사용
a = [1, 2, 3]
b =a[:] # a를 에 복사O, a와 b는 다른 변수

a[0] = 4

print(b) 

# 2. copy() 모듈을 사용

from copy import copy
a = [1, 2, 3]
b =copy(a)

# 변수를 대입하는 방법 (언팩킹)

[a,b] = ['python', 'life']
a,b = ['python', 'life']
a,b = 'python', 'life'

print(a,b)

# 변수 값을 맞바꾸기

a = 3
b = 5
a, b = b, a
print(a,b)





































