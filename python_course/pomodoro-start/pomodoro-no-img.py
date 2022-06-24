import tkinter

WORK_MIN = 25
LONG_BREAK_MIN = 20
SHORT_BREAK_MIN = 5
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
reps = 0
timer = None

def start_timer():
    global reps
    reps += 1
    if reps%2:
        title.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN*60)
    elif not reps%8:
        title.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    else:
        title.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    title.config(text="Timer", fg=GREEN)
    timer_text.config(text="00:00")
    check.config(text="")
def count_down(n):
    global timer
    timer_text.config(text=f"{n//60:0>2}:{n%60:0>2}")
    if n>0:
        timer = window.after(1000, count_down, n-1)
    else:
        if not reps%2:
            check.config(text="".join(["✔" for _ in range(reps//2)]))
        start_timer()

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50)
title = tkinter.Label(text="Timer", font=("Arial", 50, "bold"), fg=GREEN)
title.grid(row=0, column=1)
timer_text = tkinter.Label(text="00:00", font=("Arial", 50, "bold"))
timer_text.grid(row=1, column=1)
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)
check = tkinter.Label(text="", fg=GREEN)
check.grid(row=3, column=1)

window.mainloop()