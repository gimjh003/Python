def std_weight(height, gender):
    if gender == "남자":
        std_weight = (height/100)**2*22
        print(f"키 {height}cm인 남자의 표준 체중은 {std_weight:.2f}kg 입니다.")
    else:
        std_weight = (height/100)**2*21
        print(f"키 {height}cm인 여자의 표준 체중은 {std_weight:.2f}kg 입니다.")

std_weight(169, "남자")

example = [1, 2, 3, [4, [5, 6]], 7, [8, 9]]
def flatten(data):
    out = []
    if type(data) == list:
        for item in data:
            out += flatten(item) # 이 과정에서 만들어지는 리스트(리턴)들 : [1, 2, 3], [4, 5, 6] (append로 4 추가, 리스트 연산자로 5와 6 추가), [7], [8, 9]
    else:
        out.append(data)
    return out # 그리고 저 리턴들을 모조리 더해서 만들어지는 최종적인 리스트가 [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(flatten(example))