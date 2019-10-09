from tkinter import *
import OverwatchCounters
window = Tk()
window.title("Welcome to Repl.it")
window.geometry('1000x1000')

lbl = Label(window, text="Pick a Hero")
lbl.grid(column=0, row=0)

txt = Entry(window,width=20)
txt.grid(column=10, row=0)

def clickedLucio():
    lbl.configure(text="Lucio")
def clickedReinhardt():
    lbl.configure(text="Reinhardt")

btnLucio = Button(window, text="Lucio", command=clickedLucio)
btnLucio.grid(column=2, row=0)
btnReinhardt = Button(window, text="Reinhardt", command=clickedReinhardt)
btnReinhardt.grid(column=3, row=0)



window.mainloop()
