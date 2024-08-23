# if문

# 돈이 5000원 이상이며 택시, 아니면 버스를 타고 가라

money = 6000
if money > 5000 : 
    print("택시를 타고 가라")
else :
    print('버스를타고 가라')

# lf문의 구조
# if 조건문:
#  명령문
#  명령문

if True:
    print('Hello')
    print('World!')

if False:
    print('Hello')
    print('World!')
else:
    print('Hi')
    print('World!')

age = 18
if age >= 18:
    print("투표가 가능합니다")
else:
    print('투표가 불가능 합니다')

# 조건문 : 비교 연산자

x = 3
y = 2

print(x > y)
print(x < y)
print(x == y)
print(x != y)

#  조건문 : 논리 연산자 (and, or, not)
# 여러개의 조건문을 판단할 때

# x and y : x와 y가 모두 Ture일 때 Ture
# x or y : y와 x 둘 중 하나만 True이어도 True이다
# not x : x가 True이면 False이고, x가 False이면 True이다

price = 9.99
print(price > 9 and price < 10)

print(price > 10 and price < 20)

print(price > 10 or price < 20)

print(price > 10 or price < 5)

print(not price > 5)
print(not (price > 5 and price < 10))

# 

money = 2000
card = False

if money >= 5000 or card:
    print('택시를 타고가라')
else:
    print('버스를 타고 가라')        

 
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print(1 not in (1, 2, 3))

pocket = ['paper', 'cellphon', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')    


pocket = ['paper', 'cellphon', 'money']
if 'money' in pocket:
    pass
else:
    print('걸어가라')    


# 두개 이상의 조건문을 가지는 if문
# if....elif....else

pocket = ['paper', 'cellphon']
card = True

if 'money' in pocket:
    print('택시를 타고 가라')
else:
    if card :
        print('택시를 타고 가라')    
    else:
        print('걸어가라')    

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
  print("택시를 타고가라")
elif card: 
  print("택시를 타고가라")
else:
  print("걸어가라")  


# 조건부 표현식
score = 75
if score >= 60:
    message = "success"
else:
    message = 'failure'

print(message)

message = 'success' if score >= 60 else 'failer'
print(message)



















