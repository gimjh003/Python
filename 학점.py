score = int(input("예상 점수 : "))
if score >= 90:
    grade = 'A'
    if score == 100:
        grade = 'A+'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"당신의 학점은 {grade} 입니다.")