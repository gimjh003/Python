def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))

# 등차수열 1, 4, 7, 10, 13
# 첫째항이 1이고, 공차가 3인 등차수열
def sequence(n):
    if n==1: # 종료 조건
        return 1
    else:
        return sequence(n-1)+3 # n = 1 / 4, n = 2 / 7, n = 3 / 10

print(sequence(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

fibonacci_leaf = {0:0, 1:1}
def advanced_fibonacci(n):
    if n in fibonacci_leaf:
        return fibonacci_leaf[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_leaf[n] = output
        return output

print(fibonacci(5))