import random
com = random.randint(1, 1000)
tryNo = 0
player = 0
min = 1
max = 1000
while True:
    if tryNo == 0:
        player = int(input("숫자를 입력하세요 [범위 : 1 ~ 1000] : "))
        if player == com:
            print("헐")
            tryNo += 1
            break
        elif player < com:
            print("업")
            min = player+1
            tryNo += 1
        else:
            print("다운")
            max = player-1
            tryNo += 1
    else:
        player = int(input("숫자를 입력하세요 [범위 : {} ~ {}] : ".format(min, max)))
        if player == com:
            print("성공")
            tryNo += 1
            break
        elif player < com:
            print("업")
            min = player+1
            tryNo += 1
        else:
            print("다운")
            max = player-1
            tryNo += 1
print("총 시도 횟수 : {}".format(tryNo))