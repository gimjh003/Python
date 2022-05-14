class Student():
    def study(self):
        print("공부를 합니다.")
    
class Teacher:
    def teach(self):
        print("학생들을 가르칩니다.")

classroom = [Student(), Student(), Student(), Student(), Teacher()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()