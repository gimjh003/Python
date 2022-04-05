'''
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed :", file.closed)
'''
'''
try:
    file = open("info.txt", "w")
    예외.발생()
    file.close()
except Exception as e:
    print(e)
print("file closed :", file.closed)
'''
# 위 코드 실행 결과, file closed : False로 나오게 됨
# 프로그램에서 파일을 열었으면 닫아야 하니, 이 코드를 조금 변경헤서 에러가 발생해도 닫히게 할 수 있음
'''
try:
    file = open("info.txt", "w")
    예외.발생()
    file.close()
except Exception as e:
    print(e)
finally:
    file.close()
print("file closed :", file.closed)
'''
# 이렇게 할 경우 오류 발생 여부 관계없이 항상 마지막 단계에서 파일을 닫게 됨, 결과적으로 file.closed = True
# 물론 try-except 구문 뒤에 finally를 사용하지 않고 그냥 file.close()를 해서 파일을 닫는 것도 가능함

def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
        print(file.closed)

write_text_file("info.txt", "Hello, World!")

# finally의 강력한 점은, 실행 흐름에서 return을 마주한다고 해도 무조건 실행된다는 것, break를 통해 벗어난다고 해도 마찬가지임

print("프로그램 시작")
while True:
    try:
        print("try 구문 실행")
        break
        print("break 키워드 뒤")
    except:
        print("except 구문 실행")
    finally:
        print("finally 구문 실행")
    print("while 마지막 줄")
print("프로그램 종료")

numbers = [52, 273, 32, 103, 90, 10, 275]
print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {}는 {}위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("- 리스트 내부에 없는 값입니다. -")
print()
print("--- 정상적으로 종료되었습니다. ---")

# 예외 구분하기
'''
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력하세요.")
except IndexError:
    print("리스트의 인덱스를 벗어났어요.")
'''

# 예외 구분 구문과 예외 객체, 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해주세요.")
    print("exception :", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요.")
    print("exception :", exception)
except Exception as exception:
    print("예기치 못한 에러가 발생했어요.")
    print("exception :", exception)