import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {name:random.randint(0,100) for name in names}
passed_students = {name:score for (name, score) in students_scores.items() if score>=60}

print(passed_students)