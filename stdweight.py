def std_weight(height, gender):
    if gender == "남자":
        std_weight = (height/100)**2*22
        print(f"키 {height}cm인 남자의 표준 체중은 {std_weight:.2f}kg 입니다.")
    else:
        std_weight = (height/100)**2*21
        print(f"키 {height}cm인 여자의 표준 체중은 {std_weight:.2f}kg 입니다.")

std_weight(169, "남자")