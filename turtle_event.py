import turtle
win = turtle.Screen()
t = turtle.Turtle()

def click_handler(x, y): # 마우스 클릭 이벤트 핸들러는 x, y 입력 인자 필수 (클릭한 위치의 좌표가 매개변수로 들어감)
    print("클릭 이벤트 발생", x, y)

def key_handler():
    print("키 입력 이벤트 발생")

win.onclick(click_handler) # 스크린을 클릭했을 때 이벤트 발생
win.onkey(key_handler, 'space') # space키를 눌렀을 때 이벤트 발생
win.listen() # 스크린 객체가 키보드 입력을 받을 수 있도록 활성화 (onclick 메소드는 listen 메소드를 필요로 하지 않는다)