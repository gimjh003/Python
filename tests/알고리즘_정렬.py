# 임시 저장소를 활용한 데이터 교환의 기본

a = 3
b = 5
temp = a # 임시 저장소에 a값을 백업 (이러지 않으면 교환 과정에서 한 쪽의 데이터가 손실된다)
a = b
b = temp # 백업해놓았던 a값을 b값에 저장
print("a : {}, b : {}".format(a, b)) # 두 값이 바뀐 결과가 나온다.

# 하지만 파이썬에서는 임시 저장소 없이도 두 값의 교환이 가능한데, 이는 예외적인 경우이다.

a = 3
b = 5
a, b = b, a
print("a : {}, b : {}".format(a, b))

# 버블 정렬

t = [7,5,9,2,8]
# stage (0~4)
for i in range(0, len(t)-1): # -1을 하는 이유는 i번째와 i+1번째를 비교할 것이기 때문, 만약 -1을 해주지 않으면 IndexError가 raise될 것.
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]
# stage (0~3)
for i in range(0, len(t)-2): # -2를 하는 이유는 이전과 마찬가지지만 이미 이전의 정렬을 마친 후, 가장 큰 숫자가 이미 맨 뒤에 가있을 것이기 때문이다. (시간 복잡도를 줄이기 위함)
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]
# stage (0~2)
for i in range(0, len(t)-3):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]
# stage (0~1)
for i in range(0, len(t)-4):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]
print(t)

# for문으로 묶으면 이러하다

t = [7,5,9,2,8]
for j in range(1, len(t)-1):
    for i in range(0, len(t)-j): # 정렬이 완료될 경우 가장 큰 숫자가 맨 뒤에 위치하게 된다. 그러므로 정렬 대상 범위를 단계가 계속될수록 줄여줘야 하는데, 이를 위해 늘어나는 숫자(j)가 필요하다.
        if t[i] > t[i+1] : # (시작(0), 끝(len(t)의 마지막 인덱스까지)-완료된 반복 수(처음에는 0, j가 올라갈수록 범위가 좁혀짐)-1(처음반복 때 마지막-1번째 인덱스까지만(참조 오류 방지), j의 초기값이 1인 이유이기도 하다))
            t[i], t[i+1] = t[i+1], t[i]
print(t)

# stage 0 : [7, 5, 9, 2, 8] 정렬 전
# stage 1 : [5, 7, 2. 8. 9] 1번째 정렬 : j=1
# stage 2 : [5, 2, 7, 8, 9] 2번째 정렬 : j=2
# stage 3 : [2, 5, 7, 8, 9] 3번째 정렬 : j=3 ??

# 버블 정렬 알고리즘을 위해서는 n-1번의 정렬 과정이 필요하다. (정렬 과정에서 큰 수는 자연스럽게 뒤로 가게 되지만, 작은 수도 마찬가지로 점점 앞으로 오게 된다. 분명 최후의 정렬을 마치면 맨 앞은 가장 작은 수일 것(굳이 할 필요가 없음))
# 이를 위해서는 for j in range(1, len(lst))로 작성해야 한다.

# 위에 제시된 알고리즘의 문제점, 이유는 생각해보아야 한다.
test = [11,10,9,8,7,6,5,4,3,2,1]
for j in range(1, len(test)-1):
    for i in range(0, len(test)-j):
        if test[i] > test[i+1]:
            test[i], test[i+1] = test[i+1], test[i]
print(test)

# stage 0 : [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 정렬 전
# stage 1 : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11] 1번째 정렬 : j=1
# stage 2 : [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11] 2번째 정렬 : j=2
# stage 3 : [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11] 3번째 정렬 : j=3
# stage 4 : [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11] 4번째 정렬 : j=4
# stage 5 : [6, 5, 4, 3, 2, 1, 7, 8, 9, 10, 11] 5번째 정렬 : j=5
# stage 6 : [5, 4, 3, 2, 1, 6, 7, 8, 9 ,10, 11] 6번째 정렬 : j=6
# stage 7 : [4, 3, 2, 1, 5, 6, 7, 8 ,9, 10, 11] 7번째 정렬 : j=7
# stage 8 : [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11] 8번째 정렬 : j=8
# stage 9 : [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11] 9번째 정렬 : j=9 (마지막)
# stage A : [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11] A번째 정렬 : j=10 (총 10번의 정렬이 필요하지만, i 반복문에서는 9번 밖에 반복하지 못하기 때문에 오류가 일어나고 만다)
# 바깥 반복문은 반복 수를 정해주는 것이지, 단순 숫자의 패턴을 위한 것이 아니다.
# 몇 번의 반복이 필요한가? 를 정해주는 것이 바깥 반복문이라면, 얼마나 값 교환을 해야 하는가? 를 정하는 것은 안쪽 반복문이다.

# 선택 정렬 : 원소들 중 하나를 선택하여 가장 작은 걸 앞에 보낸다.
# 주어진 범위 내에서 min값의 인덱스를 구해서 리턴하는 함수

t = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def find_min(start, end):
    min = t[start]
    index = start
    for i in range(start+1, end):
        if min > t[i]:
            min = t[i]
            index = i
    return index # min값의 위치 반환

for i in range(len(t)-1):
    min_index = find_min(i, len(t))
    t[i], t[min_index] = t[min_index], t[i]

print(t)