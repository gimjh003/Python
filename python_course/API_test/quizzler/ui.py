import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = tkinter.PhotoImage(file="python_course/API_test/quizzler/images/true.png")
        false_image = tkinter.PhotoImage(file="python_course/API_test/quizzler/images/false.png")
        self.true = tkinter.Button(image=true_image, command=self.check_answer_true)
        self.true.grid(row=2, column=0)
        self.false = tkinter.Button(image=false_image, command=self.check_answer_false)
        self.false.grid(row=2, column=1)
        self.get_next()
        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quiz = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=quiz)
        else:
            self.true.config(state="disable")
            self.false.config(state="disable")
            self.canvas.itemconfig(self.question, text="You've reached the end of questions.")

    def check_answer_true(self):
        self.check_answer("True")

    def check_answer_false(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        answer = self.quiz.check_answer(user_answer)
        if answer:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next)