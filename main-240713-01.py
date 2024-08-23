# 파일 읽고 쓰기

# 파일생성

# f = open("Newfile.txt", 'w', encoding= 'utf8') # 파일을 생성한다
# f.close() # 파일을 닫는다

# 파일 열기 모드 종류

# 'w' : 쓰기모드- 파일을 새로 생성하고, 쓰기를 할때
    # 만약 같은 이름의 파일이 이미 존재 할 때 기존의 내용을 삭제하고, 쓰기 실행
# 'r' : 읽기모드- 이미 존재하는 파일을 읽기만 한다
# 'a' : 추가모드- 이미 존재하는 파일의 맨 마지막에 새로운 내용을 추가

# 파일쓰기
# f = open('Newfile.txt', 'w', encoding= 'utf8')
# for i in range(1,11):
#     data = f'{i}번째 줄입니다\n'
#     f.write(data)
# f.close()

# 파일읽기
# f = open('Newfile.txt', 'r', encoding='utf8')
# line = f.readline()
# print(line)
# f.close()


# f = open('Newfile.txt', 'r', encoding='utf8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# f = open('Newfile.txt', 'r', encoding='utf8')
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()

# 파일을 읽을 때 줄바꿈 문자를 제거하고자 할 때

# f = open('Newfile.txt', 'r', encoding='utf8')
# lines = f.readlines()
# for line in lines:
#     print(line.strip())
# f.close()

# read함수를 이용하여 파일 읽기

# f = open("newfile.txt", 'r', encoding='utf8')
# data = f.read()
# print(data)
# f.close()

# 파일 객체를이용하여 읽는 법

# f = open("newfile.txt", 'r', encoding='utf8')
# for line in f:
#     print(line)
# f.close()

# 파일에 새로운 내용을 추가하기

# f = open("newfile.txt", 'a', encoding='utf8')
# for i in range(11, 21):
#     data = f'{i}번째 줄입니다\n'
#     f.write(data)
# f.close()

# with문과 함께 사용하기





























































































































