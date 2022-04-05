'''
# 모듈을 읽어들입니다.
import sys
# 명령 매개변수를 출력합니다.
print(sys.argv)
print("---")
# 컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion() :", sys.getwindowsversion())
print("---")
print("copyright :", sys.copyright)
print("---")
print("version :", sys.version)
sys.exit()
'''

'''
import os
print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더 내부의 요소 :", os.listdir())
os.mkdir("hello")
os.rmdir("hello")
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")
os.remove("new.txt")
# os.unlink("new.txt") == os.remove("new.txt")
os.system("dir")
# os.system()은 굉장히 위험할 수 있는 함수인 동시에, 적합한 상황에 사용한다면 유용한 함수이다.
'''

'''
import datetime
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y년%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))
# 문자열, 리스트 등 앞에 *을 붙이면 요소 하나하나가 매개변수로 지정된다.
print(output_a)
print(output_b)
print(output_c)
print()
'''

'''
import datetime
now = datetime.datetime.now()
# 특정 시간 이후의 시간 구하기
print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1, \
    days=100, \
    hours=1, \
    minutes=1, \
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()
# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()
'''

# time 모듈 실험, 유닉스 시간을 구할 때, 특정 시간 동안 코드 진행을 정지할 때 많이 사용.
import time
def cool_type(str):
        for i in range(len(str)):
            print(str[i], end="")
            time.sleep(0.05) # time.sleep(5) = 5초 동안 코드 진행 정지
        print()

cool_type("안녕하세요, Hello World!")

'''
from urllib import request
# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()

print(output)
'''

'''
import os
output = os.listdir(".")
print("os.listdir() :", output)
print()
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더 :", path)
    else:
        print("파일 :", path)
'''

'''
import os
def read_folder(path):
    dirlist = os.listdir(".")
    for item in dirlist:
        if os.path.isdir(item):
            read_folder(item)
        else:
            print("파일 :", item)

read_folder(".")
'''

