from tkinter import Tk, Button, Label, DoubleVar, Entry
from lab import window

def convert():
	value=float(ft_entry.get())
	meter=value*0.3048
	mt_value.set('%.4f' % meter)
def clear():
	ft_value.set('')
	mt_value.set('')

ft_lbl=Label(window,text='Feet',bg='black',fg='white',width=14)
ft_lbl.grid(column=0,row=0,padx=20,pady=20)

ft_value= DoubleVar()
ft_entry= Entry(window,textvariable=ft_value,width=20)
ft_entry.grid(column=3,row=0)
ft_entry.delete(0,'end')

mt_lbl=Label(window,text='Meter',bg='black',fg='white',width=14)
mt_lbl.grid(column=0,row=2)

mt_value= DoubleVar()
mt_entry= Entry(window,textvariable=mt_value,width=20)
mt_entry.grid(column=3,row=2,pady=30)
mt_entry.delete(0,'end')

btn=Button(window,text='Convert',bg='blue',fg='white',width=14,command=convert)
btn.grid(column=0,row=4,padx=10,pady=30)

clr=Button(window,text='Clear',bg='blue',fg='white',width=14,command=clear)
clr.grid(column=3,row=4,pady=30,padx=10)

window.mainloop()
