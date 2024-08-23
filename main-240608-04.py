# set 집합 자료

# set 자료형을 생성하는 방법

s1 = set([1, 2, 3])
print(s1)

s2 = {1, 2, 3}
print(s2, type(s2))

# set의 특징
# 1. {}를 사용
# 2. 요소값은 중복 X
# 3. 순서가 없다(인덱싱이나 슬라이싱 사용 불가)

# set의 값을 가져오는 방법
# set을 리스트나 튜플로 변환하여, 인덱싱이나 슬라이싱 사용

s1 = {1, 2, 3, 4}
# print(s1[0]) # error

l1 = list(s1) # set을 리스츠로 변환
print(l1[0])


s1 = {1, 2, 3, 4}
t1 = tuple(s1) # set을 튜플로 변환
print(t1[0])

# set을 중복을 제거하는 fliter로 사용가능하다

lst = [1, 2, 3, 1, 2, 4, 5, 6, 4, 5, 6, 7, 8, 9]

s = set(lst) # 중복된 값 삭제
print(s)

new_lst = list(s) # 중복된 값이 제거된 리스트를 생성
print(new_lst)

# set을이용하여, 교집합, 합집합, 차집합을 쉽게 구할 수 있다

# 1. 교집합 : &

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1 .intersection(s2))

# 2. 합집합 : |

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

# 3. 차집합 : -

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

# set관련 함수

# 1. 값 1개 추가하기 : add()

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 2. 값을 여러게 추가하기 : update()

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
print(list(s1)) # set을 list로 변경

# 3. 특정 값을 제거하기 : remove()

s1 = set([1, 2, 3])
s1.remove (2)
print(s1)



































































































































