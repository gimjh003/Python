with open("study.txt", "w", encoding="utf8") as study:
    study.write("study")

with open("study.txt", "r", encoding="utf8") as study:
    print(study.read())
    print(type(study.read()))