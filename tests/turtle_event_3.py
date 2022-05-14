# 키보드 관련 이벤트
# onkey(함수, 키) : 주어진 키를 눌렀다 뗐을 때 호출되는 함수를 등록한다.
# onkeypress(함수, 키) : 주어진 키를 홀드할 때 호출될 함수를 등록한다.
# onkeyrelease(함수 키) : 주어진 키를 뗐을 때 호출될 함수를 등록한다.

# onkey랑 onkeyrelease랑 뭔가 비슷한듯.

# 화면에 출력되는 문자에 해당하는 키의 경우에는 출력되는 문자 그대로를 입력 인자로 주면 해당 키 이벤트 핸들러를 등록할 수 있다.
# 하지만 화면에 출력되지 않는 특수키의 경우, 해당키가 특정될 수 있는 이름을 사용해야 한다.

# Right : 오른쪽 화살표 키, Left : 왼쪽 화살표 키, Up : 위쪽 화살표 키, Down : 아래쪽 화살표 키, space : 스페이스 바, Escape : ESC 키, Tab : 탭 키

import turtle
win = turtle.Screen()
t = turtle.Turtle()

def turn():
    t.right(360) # 거북이 회전

win.onkeypress(turn) # 아무키나 눌리면 turn 함수 실행
win.onkeyrelease(turn, 'space') # space키를 떼면 turn 함수 실행
win.listen()