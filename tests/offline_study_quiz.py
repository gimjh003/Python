from random import *
day = randint(4, 28)
# or randrange(4, 29) // randrange() =  1부터 n미만의 값
# or int(random()*25+4) // random() = 0.0 ~ 1.0미만의 값
print("오프라인 스터디 모임 날짜는 매월 {}일로 선정되었습니다.".format(day))
print("오스모 날짜 " + str(day) + "일로 선정")