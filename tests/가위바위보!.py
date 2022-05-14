# a == 3 보다 3 == a가 실수 확률 적음
import random
pick = ['가위', '바위', '보']
c = random.choice(pick)
p = input("가위, 바위, 보 중에 하나를 선택하세요 : ")
if p not in pick:
    print("잘못된 값을 입력하셨습니다.")
else:
    print(f"내가 낸 패 : {p}\n컴퓨터 패 : {c}")
    if c==p:
        print("비겼습니다.")
    elif c=='가위' and p=='바위':
        print("이겼습니다.")
    elif c=='가위' and p=='보':
        print("졌습니다.")
    elif c=='바위' and p=='보':
        print("이겼습니다.")
    elif c=='바위' and p=='가위':
        print("졌습니다.")
    elif c=='보' and p=='가위':
        print("이겼습니다.")
    elif c=='보' and p=='바위':
        print("졌습니다.")

