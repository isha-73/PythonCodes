import tkinter as tk
r = tk.Tk()
r.title('Calculator')
r.geometry('250x250')
canvas = tk.Canvas(r,width=1000,height=1000)
canvas.pack()
num7=tk.Button(canvas, text='7', width=4).grid(row=0,column=0)
num8=tk.Button(canvas, text='8', width=4).grid(row=0,column=1)
num9=tk.Button(canvas, text='9', width=4).grid(row=0,column=2)
num4=tk.Button(canvas, text='4', width=4).grid(row=1,column=0)
num5=tk.Button(canvas, text='5', width=4).grid(row=1,column=1)
num6=tk.Button(canvas, text='6', width=4).grid(row=1,column=2)
num1=tk.Button(canvas, text='1', width=4).grid(row=2,column=0)
num2=tk.Button(canvas, text='2', width=4).grid(row=2,column=1)
num3=tk.Button(canvas, text='3', width=4).grid(row=2,column=2)
num0=tk.Button(canvas, text='0', width=4).grid(row=3,column=0)
op1=tk.Button(canvas, text='+', width=4).grid(row=0,column=3)
op2=tk.Button(canvas, text='-', width=4).grid(row=1,column=3)
op3=tk.Button(canvas, text='*', width=4).grid(row=2,column=3)
op4=tk.Button(canvas, text='/', width=4).grid(row=3,column=1)
tk.Button(canvas, text='Enter', width=4).grid(row=3, column=2)
tk.Button(canvas, text='Clear', width=4).grid(row=3, column=3)
canvas.mainloop()
r.mainloop()
