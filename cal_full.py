from tkinter import *
# from tkinter import ttk,messagebox

root=Tk()
root.geometry("350x310")
root.title("Calculator")
root.resizable(False,False)
mytxt=StringVar()

digit=''
def button(dig):
    global digit
    digit=digit+str(dig)
    mytxt.set(digit)

def all_equal():
    # global digit
    result=eval(inp1.get()) 
    # result=eval(digit)#we can also use this
    mytxt.set(result)

def clear_butn():
    global digit
    digit=" "
    mytxt.set(digit)

inp1=Entry(root,textvariable=mytxt,width=30,justify='right', bd=29,font=("Arial",10))
inp1.grid(row=0,columnspan=4)
 
butn1=Button(root,text='  7  ' ,command=lambda: button(7),bd=12).grid(row=1,column=0)
butn2=Button(root,text='  8  ' ,command=lambda: button(8),bd=12).grid(row=1,column=1)
butn3=Button(root,text='  9  ' ,command=lambda: button(9),bd=12).grid(row=1,column=2)
but1=Button(root,text=' +  ',command=lambda: button('+'),bd=12).grid(row=1,column=3)

butn4=Button(root,text='  4  ' ,command=lambda: button(4),bd=12).grid(row=2,column=0)
butn5=Button(root,text='  5  ' ,command=lambda: button(5),bd=12).grid(row=2,column=1)
butn6=Button(root,text='  6  ' ,command=lambda: button(6),bd=12).grid(row=2,column=2)
but2=Button(root,text='  -  ' ,command=lambda: button('-'),bd=12).grid(row=2,column=3)

butn7=Button(root,text='  1  ' ,command=lambda: button(1),bd=12).grid(row=3,column=0)
butn9=Button(root,text='  2  ' ,command=lambda: button(2),bd=12).grid(row=3,column=1)
butn9=Button(root,text='  3  ' ,command=lambda: button(3),bd=12).grid(row=3,column=2)
but3=Button(root,text='  x  ' ,command=lambda: button('*'),bd=12).grid(row=3,column=3)



but5=Button(root,text=' CR ' ,command=clear_butn,bd=12).grid(row=4,column=0)
butn0=Button(root,text='  0  ' ,command=lambda: button(0),bd=12).grid(row=4,column=1)
but5=Button(root,text='  =  ' ,command=all_equal,bd=12).grid(row=4,column=2)
but4=Button(root,text='  /  ' ,command=lambda: button('/'),bd=12).grid(row=4,column=3)
root.mainloop()
