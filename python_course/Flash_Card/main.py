import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = None
id = "test"

# word data extract

try:
    word_data = pandas.read_csv("python_course/Flash_Card/data/words_to_learn.csv").to_dict(orient="records")
except:
    word_data = pandas.read_csv("python_course/Flash_Card/data/english_words.csv").to_dict(orient="records")

# print

def next_card():
    global word
    global id
    word = random.choice(word_data)
    canvas.itemconfig(canvas_card, image=card_img_f)
    canvas.itemconfig(canvas_title, text="English", fill="black")
    canvas.itemconfig(canvas_word, text=word["English"], fill="black")
    window.after_cancel(id)
    id = window.after(3000, reveal)

def next_card_r():
    word_data.remove(word)
    data_frame = pandas.DataFrame(word_data)
    data_frame.to_csv("python_course/Flash_Card/data/words_to_learn.csv", index=False)
    next_card()

def reveal():
    canvas.itemconfig(canvas_card, image=card_img_b)
    canvas.itemconfig(canvas_title, text="Korean", fill="white")
    canvas.itemconfig(canvas_word, text=word["Korean"], fill="white")

# UI
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_f = tkinter.PhotoImage(file="python_course/Flash_Card/images/card_front.png")
card_img_b = tkinter.PhotoImage(file="python_course/Flash_Card/images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_img_f)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 253, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = tkinter.PhotoImage(file="python_course/Flash_Card/images/wrong.png")
wrong_btn = tkinter.Button(image=wrong_img, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = tkinter.PhotoImage(file="python_course/Flash_Card/images/right.png")
right_btn = tkinter.Button(image=right_img, command=next_card_r)
right_btn.grid(row=1, column=1)


next_card()
window.mainloop()