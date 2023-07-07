#grocery list app

from tkinter import*
window=Tk()

window.geometry("600x500")

Label(window, text="Grocery List").pack()

frame = Frame(window)
frame.pack()

listbox = Listbox(frame, width=20, height=20, font=("Helvetica", 12))
listbox.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

l=open("item_cost.txt")
for x in l:
    listbox.insert(END, str(x))
l.close()

Label(window, text="Total Cost: $477.2").pack()

window.mainloop()