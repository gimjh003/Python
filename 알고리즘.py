# 알고리즘 분석은 다음과 같은 기준들로 평가된다.
# 1. 정확성
# 2. 단위 시간당 작업량
# 3. 메모리(기억 장소) 사용량
# 4. 단순성
# 5. 최적성

# 예제 1 : 1부터 100까지의 합

# 일반적인 방법
sum = 0
for i in range(1, 100+1):
    sum += i
print(sum)

# 가우스 합계 방법
# sum = n*(n-1)/2 / 시작과 끝을 더한 값이 전체 길이의 2등분 만큼 반복됨
sum = 0
n = 100 + 1
sum = n * (n-1) / 2
print(sum)

# 수행 시간 비교

import time
sum = 0
N = 10000

start = time.time() # 시작 시각 측정
for i in range(N+1):
    sum += i
print("일반적 방법 소요시간 :", time.time()-start) # 현재시각 - 시작시각 = 지난 시간(초)
print(sum)

start = time.time()
sum = (N+1)*(N/2)
print("가우스 합 소요시간 :", time.time()-start)
print(sum)

# 예제 2 : 최대공약수 구하기

# 일반적으로 두 수의 최대공약수를 구하기 위해서는 우선 두 수의 약수를 각각 구해야 한다.
# 이후, 겹치는 약수(공약수)가 있는지 확인하고 그 중 가장 큰 값을 찾는다.

# (1) 두 수의 약수 구하기 -> factorization(n) : n의 약수를 1~n까지 반복하면서 찾은 후, 약수 리스트 반환
def factorization(n):
    f = []
    for i in range(1, n+1):
        if n%i == 0:
            f.append(i)
    return f

# (2) 두 수의 약수들 간 교집합 구하기 -> intersection(a, b) : 리스트 a, b를 입력받아 두 리스트 모두에 속한 항목들만 리스트로 반환
def intersection(a, b):
    f = []
    for i in a:
        if i in b:
            f.append(i)
    return f

# (3) 교집합 원소 중 최댓값 구하기 -> find_max(a) : a에 있는 값 중 최댓값을 반환한다.
def find_max(a):
    max = 0
    for i in a:
        if i>max:
            max = i
    return max

x = int(input("첫 번째 수 : "))
y = int(input("두 번째 수 : "))
c = intersection(factorization(x), factorization(y))
gcd = find_max(c)
print("최대공약수 :", gcd)