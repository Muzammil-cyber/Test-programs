from tkinter import *
import random

main = Tk()
main.title("Dum Dumb")
main.geometry("550x400")


def Yes():
    B1.destroy()
    B2.destroy()
    L1.config(text="I knew it")
    Button(main, text="Exit", command=lambda: main.destroy()).grid(row=1, column=4)


def No():
    column = random.randrange(0, 7)
    row = random.randrange(1, 7)
    while row == 1 and column == 1:
        column = random.randrange(0, 7)
        row = random.randrange(1, 7)

    B2.grid(column=column, row=row)


L1 = Label(main, text="Are you Dumb ?", font=("Hotch Regular", 40), pady=100, padx=100)
L1.grid(row=0, column=1, columnspan=6)
B1 = Button(main, text="Yes", font=("Dribble", 30), command=lambda: Yes())
B1.grid(row=1, column=1, padx=100)
B2 = Button(main, text="No", font=("Dribble", 30), command=lambda: No())
B2.grid(row=1, column=5)
main.mainloop()
