# 문자열은 인덱싱과 슬라이싱으로 변경할 수 없다.

a = "pithon"

# a[1] = "y" # 불가하다. error가 발생
 
 # print(a)

a = a[:1] + "y" + a[2:]

print(a)

