for i in range(1, 51):
    with open(f"{i}주차.txt", "w", encoding="utf8") as File:
        File.write(f"- {i}주차 업무 보고 -\n부서 : 보안관제\n이름 : 김정협\n특이사항 : 없음")