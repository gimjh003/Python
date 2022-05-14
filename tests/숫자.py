from cgitb import small


numbers = [1,3,2,4,5,6,4,3,7,6,0,8,9,4,5,6,3,2,4,5,6,7,3,2,1]
dic = {}
for number in numbers:
    if number not in dic:
        dic[number] = 1
    else:
        dic[number] += 1

print(dic)

pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

# 출력 결과 : {name} {age}살\n

for pet in pets:
    print(pet["name"], str(pet["age"])+"살")

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {"sword" : "밤과 불꽃의 검", "armor" : "풀플레이트"},
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for lst in character[key]:
            print(key, ":", lst)
    else:
        print(key, ":", character[key])