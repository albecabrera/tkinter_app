from tkinter import *
root = Tk()

titulo1 = Label(root, text="Noroeste").pack(anchor=NW)
titulo2 = Label(root, text="NoRte").pack(anchor=N)
titulo3 = Label(root, text="Noreste").pack(anchor=NE)
titulo4 = Label(root, text="Oeste").pack(anchor=W)
titulo5 = Label(root, text="Centro").pack(anchor=CENTER)
titulo6 = Label(root, text="Este").pack(anchor=E)
titulo7= Label(root, text="Sudoeste").pack(anchor=SW)
titulo8 = Label(root, text="Sud").pack(anchor=S)
titulo9 = Label(root, text="Sudeste").pack(anchor=SE)

mainloop()

root.mainloop()