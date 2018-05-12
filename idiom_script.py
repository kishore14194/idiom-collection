from idiom_database import Idiom, session
from tkinter import *
from random import randint
import time

query_idiom = session.query(Idiom)
all_idiom = query_idiom.all()
idiom_len = len(all_idiom)

displayed_values = []

while True:

    if len(displayed_values) == idiom_len:
        displayed_values.clear()

    rand_num = randint(1, idiom_len)
    if rand_num in displayed_values:
        continue

    print(displayed_values)
    displayed_values.append(rand_num)

    idiom_val = all_idiom[rand_num]

    window = Tk()

    window.wm_title("Learn some Idioms Dumbass !!!")
    window.geometry("400x200")

    l1 = Label(window, text=idiom_val.word, fg="red", font=("Helvetica", 20)).pack(pady=10)

    l1 = Label(window, text=idiom_val.meaning, fg="green", font=("Arial", 18)).pack(pady=10)

    window.mainloop()
    window.after(10000, lambda: window.destroy())

    time.sleep(3600)
