# %d : 정수
str = 'I eat %d apples.' % 3
print(str)
# %s : 문자열
str = 'I eat %s apples' % 'five'
print(str)


# 변수도 대입이 가능하다

number = 3
str = 'I eat %d apples.' % number
print(str)

string = 'five'
str = 'I eat %s apples.' % string
print(str)

# 여러가지를 대입하는 경우
number = 10
day = 'three'
str = ' I eat %d apples. So I was sick for %s days.' % (number, day)
print(str)

# %s에는 어떠한 값을 넣어도 됨.
print('I have %s apples.' % 3)
print('rate is %s apples.' % 3.14)

# %를 문자열 안에 넣고 싶을 때 : %%
print('error is %d%%' % 98)

# %f는 실수에 사용한다.
print('원주율은 %f 입니다.' % 3.14)


