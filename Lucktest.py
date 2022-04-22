import random
import time
user_num = int(input("1~100중에 하나의 숫자를 입력하세요 : "))
rand_num = random.randint(1, 100)
user_luck = 100
while user_num!=rand_num:
    user_luck -= 1
    print("행운의 숫자 : {0}, 선택한 숫자 : {1}, 현재 운 수치 : {2}".format(rand_num, user_num, user_luck))
    rand_num = random.randint(1, 100)
    time.sleep(2)
print("행운의 숫자와 선택한 숫자 {0}이 일치합니다.\n현재 운 수치 : {1}\n---결과---")
if user_luck==100:
    print("완벽한 날")
elif user_luck>=90:
    print("행운 최고조")
elif user_luck>=80:
    print("느낌이 좋은 날")
elif user_luck>=70:
    print("발걸음이 가벼운 날")
elif user_luck>=60:
    print("무사히 하루를 보낼 수 있는 날")
elif user_luck>=50:
    print("보통")
elif user_luck>=40:
    print("느낌이 안좋은 날")
elif user_luck>=30:
    print("불편한 날")
elif user_luck>=20:
    print("처참한 하루")
elif user_luck>=10:
    print("조심하세요")
elif user_luck>=0:
    print("유갑입니다")
else:
    print("살아서 돌아올 수 없는 날")