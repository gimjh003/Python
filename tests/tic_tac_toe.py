# 선공일 때 9 -> 1 -> 7 -> 8 하면 무조건 이김
import random

# 게임판 그리기
b = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def draw_board():
    print("-------")
    print(' '+b[1]+'|'+b[2]+'|'+b[3])
    print("-------")
    print(' '+b[4]+'|'+b[5]+'|'+b[6])
    print("-------")
    print(' '+b[7]+'|'+b[8]+'|'+b[9])
    print("-------")

# 빈칸 여부 확인
def is_free(i):
    return b[i] == ' '

# 승리 조건 확인
def check_for_win(c):
    if ((b[1]==c and b[2]==c and b[3]==c) or
        (b[4]==c and b[5]==c and b[6]==c) or
        (b[7]==c and b[8]==c and b[9]==c) or
        (b[1]==c and b[4]==c and b[7]==c) or
        (b[2]==c and b[5]==c and b[8]==c) or
        (b[3]==c and b[6]==c and b[9]==c) or
        (b[1]==c and b[5]==c and b[9]==c) or
        (b[3]==c and b[5]==c and b[7]==c)):
        return True
    else:
        return False

# 무승부 조건 확인
def check_for_draw():
    for i in range(1, 10):
        if is_free(i):
            return False
    return True

# 사용자 턴 체크
def user_turn():
    loc = int(input("당신의 수는? (1~9) : "))
    while is_free(loc) == False:
        loc = int(input("당신의 수는? (1~9) : "))
    return loc

# 컴퓨터 턴
def com_turn():
    # 미리 패를 두고 이기는 조건에 맞는다면 그대로 유지 (이기는 곳에 수를 두어야 한다)
    for i in range(1, 10):
        if is_free(i):
            b[i] = 'O'
            if check_for_win('O'):
                return i
            else:
                b[i] = ' ' # 만약 이기는 조건에 아무것도 부합하지 않는다면 다음 반복으로 넘어간다.
    # 이기는 패가 없으므로 수비에 집중한다.
    for i in range(1, 10):
        if is_free(i):
            b[i] = 'X'
            if check_for_win('X'): # 여기서 참이 된다면 이미 사람이 이겼다는 뜻 아닌가?
                return i
            else:
                b[i] = ' '
    # 승부가 갈리는 상황이 아니라면 좋은 위치를 선점해야 한다.
    if is_free(5):
        return 5
    
    for i in [1, 3, 7, 9]: # 대각선이 비었으면 선점
        if is_free(i): return i
    
    for i in [2, 4, 6, 8]: # 나머지 칸 선점
        if is_free(i): return i

print("Welcome to Tic Tac Toe Game!!")
rand = random.randint(0, 1)
if rand == 0:
    turn = 'X'
else:
    turn = 'O'

while True:
    draw_board()
    if turn == 'X':
        b[user_turn()] = 'X'
    else:
        b[com_turn()] = 'O'
    if check_for_win(turn):
        draw_board()
        print(turn+' Win')
        break
    else:
        if check_for_draw():
            draw_board()
            print('Draw')
            break
        else:
            if turn == 'X' : turn = 'O'
            else: turn = 'X'