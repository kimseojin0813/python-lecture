# # 함수 (function)


# #def 함수의 이름(매개변수,매개변수......):
# #   명령어
# #   명령어
# #   ....
# #   return 문

# # 두개의 정수를 입력받아서, 그 합을 변환하는함수를 정의
# def add(num1, num2):
#     return num1 + num2

# result = add(3, 4)
# print(result)

# result2 = add(5, 10)
# print(result2)

# # 함수의 기본형태 4가지

# # 1. 매개볌수가 없고, return 문도 없는 함수

# def printHello():
#     print('Hello....')

# printHello()

# # 2. 매개변수는 있지만, return 문은 없는 함수

# def printSum(a, b):
#     print(a+b)

# printSum(3, 7)

# # 3. 매개변수는 없지만, return 문은 있는 함수

# def rturnHello():
#     return 'Hello'

# result = rturnHello()

# print(result)

# # 4. 매개변수도 있고 return 문도 있는 함수

# def calc(a,b):
#     return a * b

# a = calc(2, 5)
# print(a)

# a = calc(3, 9)
# print(a)


# # 함수의 매개변수 : 함수를 실행하기 위해 함수 호출 시에 함수에 전달되는 값들...

# def calcs(a, b, c):
#     val = a + b
#     val = val * c
#     return val

# a = calcs(2, 3, 4)
# print(a)

# # 매개변수를 지정하여 함수를 호출하기

# def sub(a, b):
#  return a - b

# result = sub(10, 3)
# print(result)

# # 함수의 매개변수가 몇개가 될지 모를 경우 : *args 를 사용한다

# def sum(*args):
#     val = 0
#     for i in args:
#         val += i #val = val + i

#     return val

# result = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)


# # 위치 매개변수와 *args를 혼합해서 사용한 경우

# def add(choice, * args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result += i
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result *= i
#     return result

# total = add('add', 1, 2, 3, 4 ,5)
# print(total)

# total = add('mul', 1, 2, 3, 4 ,5)
# print(total)


# # 키워드 매개변수 : **kwargs -> 매개변수가 딕션너리 행태로 전달

# def printaa(**kwargs):
#     print(kwargs)

# printaa(a =1)
# printaa(name = 'jhon', age = 18)


# # 예제

# def printsa(**kwargs):
#     for i in kwargs:
#         print(f'{i} : {kwargs[i]}' )

# printsa(봄 = '딸기', 여름 = '수박', 가을 = '사과')


# # 함수에서 return문의 이해

# # 1. 함수의 return문은 한번만 적용됨
# #   함수가 return문을 만나면 그 함수를 종료한다.

# def calc(a, b):
#     return
#     return a + b
#     return a * b

# result = calc(3, 4)
# print(result)

# def calc(choice, *args):
#     if choice == "add":
#         total = 0 
#         for i in args:
#             total += i
#         return total
#     elif choice == "mul":
#         total = 1 
#         for i in args:
#             total *= i 
#         return total

# # 여러개의 값을 return하는 함수
# # 언팩킹

# def add_mul(a, b):
#     sum = a + b
#     mul = a * b
#     return sum, mul

# # val1, val2 = add_mul(3, 4)
# # print(val1, val2)
# result = add_mul(3, 4)
# print(result)

# # return문에 반환 값이 없는 경우

# def say_nick(nick):
#     if nick == "바보":
#         return
#     print(f'너의 별명은 {nick}이다')

# say_nick('홍길동')
# say_nick('바보')

# # 매개변수에 기본값(default)을 정해주기

# def say_nick(name, age, man=True):
#     print(f'나의 이름은 { name} 입니다')
#     print(f'나의 나이은 {age} 입니다')
#     if man:
#         print('나는 남자입니다')
#     else:
#         print('나는 여자입니다')

# say_nick('홍길동', 17)
# say_nick('춘향이', 17, False)

# 함수 안에서 선언된 변수에 변수의 효력 범위

# 함수 안에서 선언된 변수는 함수 안에서만 사용할 수 있다

# 함수안에서 선언된 변수를 함수 밖에서 사용하려고 하면 오류 발생

def vartest(a):
    a = a + 1
    return a

print(vartest(3))

# print(a) # 함수 안에 있는 a에 접근하려고 하면 오류 발생

# 함수 안에서 함수 밖에서 선언한 변수 사용하기

# 1. 단순히 함수 바깥의 값을 참조하기

age = 17 # 함수 바깥에서 선언한 변수 : 글로번 함수
def printage():
    print(age + 1)

printage()

# 2. 함수 바깥에서 선언된 변수를 수전하고자 할 경우 반드시 global 이란 키워드 선언

age =17

def printage():
    global age
    age = age + 1
    print(age)

printage()

# lambda(람다) 함수
# 간단한 함수를 def를 사용하지 않고 함수를 선언 하는 방법

# 함수이름 = lambda 매개변수1, 매개변수2....: 매개변수를 이용하는 표현식

add = lambda a, b: a + b

# def add(a, b):
#     return a + b
result = add(3, 4)
print(result)







































































































































