# 반복문
# while or for 사용합니다.

# while 조건:
#   조건이 참인 동안 반복 수행할 코드
#   ...

# for 조건:
#   조건이 참인 동안 반복 수행할 코드 (반복하는 횟수가 정해져 있을 때 주로 사용)

i = 0
while i < 5:
    print(f"환영합니다. [반복 횟수 : {i}]")
    i += 1
print("반복 끝")

print(list(range(0, 10, 2)))

for x in ['cs', 'u', 20]:
    print(x)

for x in range(10, 2, -3):
    print(x)

for x in range(3, 5):
    print(x)

for x in range(3):
    print(x)

for x in "Hello, World!":
    print(x, end="")