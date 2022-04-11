# 위의 별무리경기장에서의 경주는 서로 동시에 움직이는 것처럼 보이게 하는 착시이다.
# 각각의 객체를 진짜로 동시에 움직일 수는 없을까?
# 스레드(thread)는 프로그램의 실행 흐름을 독립적으로 가지고 있는 것으로, 여러 개의 스레드를 생성하면 작업을 병렬적으로 처리할 수 있다.
# 이를 다중 스레드라고 한다.

def thread1():
    for i in range(1, 5):
        print("1 ")

def thread2():
    for i in range(1, 5):
        print("2 ")

def thread3():
    for i in range(1, 5):
        print("3 ")

import threading
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t3 = threading.Thread(target=thread3)

t1.start()
t2.start()
t3.start()