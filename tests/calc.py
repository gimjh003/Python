try:
    print("나누기 전용 계산기입니다.")
    nums = []

    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError as err:
    print(f"잘못된 값을 입력하셨습니다. : {err}")
except ZeroDivisionError as err:
    print(f"0으로 나눌 수 없습니다. : {err}")
except Exception as err:
    print(f"알 수 없는 오류가 발생했습니다. : {err}")