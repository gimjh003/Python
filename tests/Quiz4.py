class Word:
    def __init__(self, nw, e1, e2, c):
        self.nw = nw
        self.e1 = e1
        self.e2 = e2
        self.c = c
    def show_question(self):
        print(f"\"{self.nw}\"의 뜻은?\n1. {self.e1}\n2. {self.e2}")
    def check_answer(self, c):
        if self.c == c:
            print("정답입니다.")
        else:
            print("틀렸습니다.")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("==> ")))