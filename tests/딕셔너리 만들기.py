key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}

for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)

limit = 10000
i=1
sum_value = 0
while sum_value < 10000:
    sum_value += i
    i += 1
print("{}를 더할 때 {}를 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(1, 100+1):
    j = 100-i
    if i*j > max_value:
        max_value = i*j
        a = i
        b = j
    
print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))

numbers = [1,2,3,4,5,6,7,8,9]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

def factorial(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

print(factorial(10))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

# 피보나치 수열 n번째 값?
#  1 1 2 3 5 8 13 21 34 55 89

'''
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else :
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(35))
'''
'''
counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(10)
print("---")
print("fibonacci(10)계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))
'''
# ↑ tree


# save value in dic = memo
'''
dictionary = {1:1, 2:1}

def fibonacci(n):
    if n in dictionary: # if memoed, return val
        return dictionary[n]
    else: # not memoed, calc val
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print("fibonacci(10) : {}".format(fibonacci(35)))
'''
dictionary = {1:1, 2:1}
# 조기 리턴
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output

print("fibonacci(35) :", fibonacci(35))

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else: output.append(item)
    return output
    

example = [[1,2,3], [4, [5, 6]], 7, [8, 9]]

print("원본 :", example)
print("변환 :", flatten(example))

# 모든 경우의 수 구하기
# EX : 6명이 식당에 가면, 2명+2명+2명, 3명+3명, 2명+4명, 6명 총 네 가지 경우의 수가 있음

앉힐수있는최소사람수 = 2 # 한 명만 앉게 하고 싶지는 않다는 조건
앉힐수있는최대사람수 = 6
전체사람의수 = 6
memo = {}
def 문제(남은사람수, 앉힌사람수): # 남은사람수와 앉힌사람수를 입력받음 if 6, 2
    key = str([남은사람수, 앉힌사람수]) # ? key = '[6, 2]'
    # 종료 조건
    if key in memo: # memo에 같은 조합이 있는지 확인함 (있으면 그거 리턴하고 종료)
        return memo[key]
    if 남은사람수 < 0: # 무효이므로 0 리턴 (종료)
        return 0
    if 남은사람수 == 0: # 수를 세기 위해 1 리턴 (남은 사람수가 0이라면 분명 하나의 경우의 수가 완성이 된 상태이기 때문일 것, 종료)
        return 1
    # 재귀 처리 (초기 매개변수를 입력받고 실질적으로 실행되는 부분)
    count = 0 # 경우의 수를 세기 위한 count 변수 선언 및 초기화
    for i in range(앉힌사람수, 앉힐수있는최대사람수+1): # [2,3,4,5,6], i에는 최대로 앉을 수 있는 사람 수에서 하나씩 줄어드는 값이 들어감 (좌석 분배를 위해) 
        count += 문제(남은사람수-i, i) # count += 문제[4, 2], 문제[3, 3], 문제[2, 4], 문제[1, 5], 문제[0, 6] ... 이 패턴은?
    # 메모화 처리수
    memo[key] = count # memo['[6, 2]'] = 경우의 수
    # 종료
    return count

# 재귀함수 이용한 문제 (p.244 2번 문제) 염두할 것, 접근 방법 : 손으로 직접 써보기

print(문제(전체사람의수, 앉힐수있는최소사람수))