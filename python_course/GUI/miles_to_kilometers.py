import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=5)
entry.grid(row=0, column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

to = tkinter.Label(text="is equal to")
to.grid(row=1, column=0)

out = tkinter.Label(text="0")
out.grid(row=1, column=1)

kilometers = tkinter.Label(text="Km")
kilometers.grid(row=1, column=2)

def calc():
    miles = float(entry.get())
    kilometers = miles*1.609
    out.config(text=kilometers)

convert = tkinter.Button(text="Calculate", command=calc)
convert.grid(row=2, column=1)

window.mainloop()