for i in range(1, 51):
    with open(f"{i}주차.txt", "w", encoding="utf8") as file:
        file.write(f"- {i}주차 주간 보고 -\n부서 : 보안관제\n이름 : 김정협\n업무 요약 : 이상 없음")
