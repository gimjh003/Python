'''
# 함수 데코레이터를 생성합니다.
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper
#... 함수에 함수를 덧씌우는 함수?

# 데코레이터를 붙여 함수를 만듭니다.
@test
def bye():
    print("good bye")
def hello():
    print("hello")

# 함수를 호출합니다.
hello()

hello()

bye(); bye()
'''

'''
from functools import wraps

def test(function):
    @wraps(function)

def wrapper(*arg, **kargs):
    print("인사가 시작되었습니다.")
    function(*arg, **kargs)
    print("인사가 종료되었습니다.")
    return wrapper
'''

# 소수 찾기

from primePy import primes
count = 0
for i in range(100, 1001):
    if primes.check(i):
        count += 1
print(count)
