import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if not reps%8:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps%2:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    time = f"{count//60:0>2}:{count%60:0>2}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if not reps%2:
            check.config(text="".join(["✔" for _ in range(reps//2)]))
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

canvas = tkinter.Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="python_course/pomodoro-start/tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

startBtn = tkinter.Button(text="Start", command=start_timer)
startBtn.grid(row=2, column=0)

resetBtn = tkinter.Button(text="Reset", command=reset_timer)
resetBtn.grid(row=2, column=2)

check = tkinter.Label(bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()