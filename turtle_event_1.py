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

# onclick()은 Screen 객체와 Turtle 객체 둘 다 가자고 있으나, onkey()는 Screen 객체에만 있다. 또한 키보드 이벤트 입력을 받기 위해서는 코드 마지막에 listen()을 호출해야만 한다.

# 클릭(click), 드래그(drag), 릴리즈(release)와 같은 마우스 관련 이벤트의 이벤트 핸들러는 반드시 마우스 커서 위치를 나타내는 x, y 입력 인자를 필수적으로 가져야 한다.

# 또한 '버튼 번호'는 3-버튼 마우스의 경우 좌클릭 1번, 휠클릭 2번, 우클릭 3번이다.

# 2-버튼 마우스의 경우 좌클릭 1번, 우클릭 2번이다.

# 버튼 번호를 생략할 경우, 자동으로 1번 버튼(좌클릭)이 적용된다.

# onclick(함수, 버튼 번호)
# onrelease(함수, 버튼 번호)
# ondrag(함수, 버튼 번호)

# onclick()은 배경 윈도우 객체와 거북이 객체 모두 가지고 있으나, onrelease()와 ondrag()는 거북이 객체만 가지고 있는 명령이다.