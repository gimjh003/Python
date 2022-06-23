import tkinter

# window
window = tkinter.Tk()
window.title("GUI programming")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="Hello, World!", font=("Arial", 24, "bold"))
my_label.pack(expand=True)
my_label.pack()

# Button
def button_clicked():
    if my_label["text"] == "Hello, World!":
        my_label.config(text=input.get())
    else:
        my_label["text"] = "Hello, World!"

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=33)
input.pack()

window.mainloop()