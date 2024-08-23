# 리스트 관련 함수

# 1. 리스트에요소 추가하기 :append() 함수
# append() 함수는 리스트의 맨 마지막에 값을 추가한다

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6]) # 중첩리스트로 추가된다
print(a)

# 리스트의 정렬 : sort() 함수

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['b', 'a', 'c']
a.sort()
print(a)

#  3. 리스트의 순서 뒤집기 : reverse() 함수

a = ['a', 'c', 'b']
a.sort()
a.reverse()
print(a)

# 4 리스트에 인덱스를 반환 : index() 함수
 
a = [1, 2, 3]
print(a.index(3))
print(a.index(2))
 # print(a.index(0)) # error 발생

 # 5 리스트에 요소를 삽입 : insert() 함수 
 # insert(인덱스, 값) : 인덱스 위치에 값을 삽입

a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(2, 6)
print(a)

# 6 리스트의 요소를 제거 : remove() 함수
# remove()함수는 첫번째 동일한 값만 제거한다

a = ['a', 'b', 'c', 'b', 'e']
a.remove('b')
print(a)

# 7 리스트 요소르 반환 하기 : pop() 함수
#리스트의 맨 마지막 요소를 반환한다 

a = [1, 2, 3]
result = a.pop() # 매개변수가 없는 경우, 맨 마지막 값을 반환
print(result)
print(a)

a = [1, 2, 3]
result = a.pop(1) # 매개변수는 인덱스 값을 가리킨다
print(result)
print(a)

# 8 리스트에 포함된 요소값 갯수 찾기 : count() 함수

a = ['a', 'b', 'c', 'b', 'e']
print(a.count('b'))

# 9 리스트의 확장 : extend
# extend() 함수의 매개변수는 리스트만 가능하다

a = [1, 2, 3]
a.extend([4, 5])
print(a)


























































































































































