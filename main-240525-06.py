# 문자열 슬라이싱
# 문법 : 문자열변수[시작인덱스:끝인덱스]
# 끝 인덱스의 문자는 포함하지 않는다 (끝 인덱스 앞까지)

a = "Life is too short, you need Python"

print(a[0:4])
print(a[8:11])
print(a[12:17])

# 만약, 시작인덱스르 생략하면  0과 같다 즉 문자열의 처음부터
# 만약, 끝인덱스르 생략하면, 문자열의 마지막까지

print(a[:17])    # a[0:17]
print(a[19:])    # a[19:0]
print(a[:])      # 처음부터 끝까지
print(a[:])      # 처음부터 끝까지
print(a)         # 이것은 문자열을 스라이싱한 것이 아니다

# 슬라이싱 예제

a = "20230331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

year = a[0:4]
month = a[4:6]
day = a[6:8]

print(year)
print(month)
print(day)



