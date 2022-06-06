class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True
    def next(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)? : ")
        self.check_answer(answer, current_question.answer)
    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was : {correct}.")
        print(f"Your current score is : {self.score}/{self.question_number}\n")