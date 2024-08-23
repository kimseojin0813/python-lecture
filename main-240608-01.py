# 튜플(tuple)
# 리스트와 유사하지만, 아래와 같이 다르다.
# 리스트는 요소값을 변경할수 있지만, 튜플은 변경 불가능하다
# 리스트는[], 튜플은 ()

# 튜플의 정의 방법

t1 = () # 빈 튜플을 정의 
t2 = (1,) # 튜플의 요소값이 하나면 존재할 때, 반드시 (,) 를 줘야 된다
t3 = (1, 2, 3,) # 요소값이 정수인 튜플 정의
t4 = 1, 2, 3 # 즉, 튜플을 정의 할때, 괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd')) # 중첩 튜플을 가질 수 있다.

# 튜플의 인덱싱

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 튜플의 슬라이싱

t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 튜플의 더하기

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# 튜플의 곱하기

t = (3, 4)
t1 = t * 3
print(t1)

# 튜플의 길이 구하기

t1 = (1, 2, 'a', 'b')
print(len(t1))






