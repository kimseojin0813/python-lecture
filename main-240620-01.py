# while 문 : 반복문

# 문장을 여러번 반복할때 사용


# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print('나무 넘어 갑니다')


# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# ... Enter number: """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# while  True:
#     money = int(input("돈을 넣어 주세요:"))
#     if money == 300:
#         print('커피를 줍시다.')
#         coffee = coffee - 1
#     elif money > 300:
#         print('거스름돈 %d를 주고 커피를 줍시다.' % (money - 300))    
#         coffee = coffee - 1
#     else:
#         print('돈을 다시 돌려주고 커피를 주지 않습니다.')    
#         print('남은 커피의 양은 %d개 입니다.' % coffee)
#     if coffee == 0:
#         print('커피가 다 떨어 졌습니다. 판매를 중지 합니다.')    
#         break

#  continue 

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:
#         continue
#     print(a)

# for 문

# 1. 전형적인 for문

# test_list = ['one', 'two', 'three'] 
# for i in test_list: 
#     print(i)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in my_list:
#      if i % 2 == 1:
#           print(i)
          

# for i in my_list[::2]:
#     print(i)
     

# for i in my_list[1::2]:
#     print(i)
     

# for문의 사용 방법
# 언팩킹 사용

# a = [(1, 2), (3, 4,), (5, 6)]

# for (first, last) in a:
#     print(first, last)

# 사용 예

# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#         print(f'{number}번 학생은 합격입니다.')
#     else:
#         print("%d번 학생은 불합격입니다." % number)    
#         print(f'{number}번 학생은 불합격입니다.')


# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         continue
#     print(f'{number}번 학생은 합격입니다.')

# for문과 함께 사용하는 range문
# range() : 리스트, 문자, 숫자 등을 자동으로 생성해 주는 함수
# range(시작, 끝, step) : 끝은 포함하지 않는다.

# a = range(0, 10)
# print(a)
# print(list(a))
# print(tuple(a))

# a = range(1, 11)
# print(list(a))

# a = range(2, 10, 2)
# print(list(a))

# a = range(10, 0, -1)
# print(list(a))

# 1부터 10까지 합을 구하라

# add = 0 

# for i in range(1, 11):
#     add = add + i
# print(add)    

# range문을 사용하여 합격 출력하기 

# marks = [90, 25, 67, 45, 80]

# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print(f'{number + 1}번 학생은 합격입니다.')

# 구구단 출력하기

# for i in range(2, 10):
#     print(f'----------{i}단-----------')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j}')
       
# 리스트 컴프리핸션

# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num*3) 

# print(result)    

a = [1, 2, 3, 4]

# result = [num*3 for num in a]
# print(result)


# result = [num*3 for num in a if num % 2 == 0]
# print(result)

# result = [x * y for x in range(2, 10) for y in range(1, 10)]
# print(result)























































































































































































