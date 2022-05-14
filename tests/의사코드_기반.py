# === 0부터 양수 입력 값까지의 홀수를 출력하는 프로그램 ===
# 1. num에 0을 저장
# 2. 키보드로 양수를 입력 받아 N에 저장
# 3. num 1 증가
# 4. num이 N보다 크면 프로그램 종료
# 5. num 나누기 2의 나머지가 1이면 num 출력
# 6. 그렇지 않으면 3번 단계로 이동

# 1. num ← 0
# 2. get N
# 3. num ← num+1
# 4. if num > N, then exit
# 5. if num % 2, then print num
# 6. else, goto step 3

num = 0
N = int(input())
while True:
     num += 1
     if num>N:
         break
     if num%2:
          print(num)

# === 1부터 양수 입력 값까지의 합을 출력하는 프로그램 ===
# 1. num에 0을 저장
# 2. sum에 0을 저장
# 3. 키보드로 양수를 입력 받아 N에 저장
# 4. num 1 증가
# 5. num이 N보다 크면 8로 이동
# 6. sum에 num을 더하기
# 7. 4로 이동
# 8. sum 출력

# 1. num ← 0
# 2. sum ← 0
# 3. get N
# 4. num ← num + 1
# 5. if num > N, then goto step 8
# 6. sum ← sum + num
# 7. goto step 4
# 8. print sum

num = 0
sum = 0
N = int(input())
while True:
    num += 1
    if num > N:
        break
    sum += num
print(sum)

# 반복 횟수가 입력 값에 의해 정해지는 반복문이므로 for문이 더 적절하다

sum = 0
N = int(input())
for i in range(1, N+1):
    sum += i
print(sum)

# === 주어진 리스트 내 최댓값을 출력하는 프로그램 ===
# 1. max에 0을 저장 (max에 0 대신 리스트의 첫 번째 항목(list[0])을 넣어도 된다)
# 2. 리스트에서 항목을 하나 꺼내어 i에 저장
# 3. i가 max보다 크면 max에 i 저장
# 4. 2로 이동
# 5. max 출력

# 1. max ← 0 or max ← list[0]
# 2. for each i in list
# 3.    if i > max, them max ← i
# 4. print max

temp = [3,5,1,9,2,13,4,7,11]
max = temp[0]
for i in temp:
    if i > max:
        max = i
print(max)

# === 주어진 리스트 내 최솟값을 출력하는 프로그램 ===
# 1. min에 list[0]를 저장 (list[0]대신 시스템에서 표현할 수 있는 가장 큰 수(sys모듈 내 maxsize)를 넣어도 된다)
# 2. 리스트에서 숫자 하나 꺼내어 i에 저장
# 3. i가 min보다 작으면 min에 i 저장
# 4. 2로 이동
# 5. min 출력

# 1. min ← list[0]
# 2. for each i in list
# 4.    if i < min, then min ← i
# 5. print min

temp = [3,5,1,9,2,13,4,7,11]
min = temp[0]
for i in temp:
    if i<min:
        min = i
print(min)