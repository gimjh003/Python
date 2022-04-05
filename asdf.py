numbers = list(range(1, 10+1))
print("# 홀수만 출력하기")
print(list(filter(lambda n: n%2 == 1, numbers)))
print()
print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda n: 2<n<7, numbers)))
print()
print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda n: n**2<50, numbers)))


n = input("input number > ")
if n.isdigit():
    n = int(n)
    print("your number is : {}".format(n))
else:
    print("error occured. please try again.")


try:
    n = int(input("input number > "))
    print("your number is : {}".format(n))
except:
    pass


list_input_a = ["52", "273", "32", "스파이", "103"]
list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
print(list_number)

try:
    number_input_a = int(input("정수 입력 : "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a*2*3.14)
    print("원의 넓이 :", number_input_a**2*3.14)

try:
    number_input_a = int(input("정수 입력 > "))
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a*2*3.14)
    print("원의 넓이 :", number_input_a**2*3.14)
except:
    print("정수를 입력해달라고 했잖아요!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

    # try 구문은 단독으로 사용할 수 없으며, 반드시 except 구문 또는 finally 구문과 함께 사용해야 한다.
    # else 구문은 반드시 except 구문 뒤에 사용해야 한다.
    # 가능한 조합 - try + except, try + except + else, try + except + finally, try + except + else + finally, try + finally