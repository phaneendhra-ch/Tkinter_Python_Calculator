'''

    A well designed Calculater App built using Python (Tkinter)

    Author : Phaneendhra


'''



from tkinter import *
import math as m
import re
import time

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    print(operator," ",type(operator)," ",len(operator))
    text_Input.set(operator)

def btnClearDisp():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    try :
        global operator
        sumup=str(eval(operator))
        print(sumup," ",type(sumup))
        text_Input.set(sumup)
        operator=sumup
    except :
        operator = "ERROR"
        text_Input.set(operator)
        operator=""

def RemoveLast():
    global operator
    if (type(operator) == float):
        operator = "Clear the Calculator"
        text_Input.set(operator)
        operator=""
    operator = list(operator)
    if (len(operator) > 0):
        del(operator[-1])
        operator = "".join(operator)
        text_Input.set(operator)
    else:
        operator=""
        text_Input.set(operator)
    
def SinF():
    global operator
    if (operator == ""):
        text_Input.set("Enter the value")
        operator=""
    else:
        operator = m.sin(float(operator))
        print(operator," ",type(operator))
        operator = str(operator)
        text_Input.set(operator)

def CosF():
    global operator
    if (operator == ""):
        text_Input.set("Enter the value")
        operator=""    
    else :
        operator = m.cos(float(operator))
        operator = str(operator)
        text_Input.set(operator)

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(
    cal,
    font=('arial', 20, 'bold'),
    textvariable=text_Input,
    bd=60,
    insertwidth=7,
    bg="yellow",
    justify='right'
).grid(columnspan=4)

num_7 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='7',command=lambda:btnClick(7)).grid(row=1,column=0)

num_8 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='8',command=lambda:btnClick(8)).grid(row=1,column=1)

num_9 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='9',command=lambda:btnClick(9)).grid(row=1,column=2)

addition = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='+',command=lambda:btnClick("+")).grid(row=1,column=3)



num_4 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='4',command=lambda:btnClick(4)).grid(row=2,column=0)

num_5 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='5',command=lambda:btnClick(5)).grid(row=2,column=1)

num_6 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='6',command=lambda:btnClick(6)).grid(row=2,column=2)

substaction = Button(cal,padx=18,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='-',command=lambda:btnClick("-")).grid(row=2,column=3)


num_1 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='1',command=lambda:btnClick(1)).grid(row=3,column=0)

num_2 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='2',command=lambda:btnClick(2)).grid(row=3,column=1)

num_3 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='3',command=lambda:btnClick(3)).grid(row=3,column=2)

multiplication = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='*',command=lambda:btnClick("*")).grid(row=3,column=3)


num_0 = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='0',command=lambda:btnClick(0)).grid(row=4,column=0)

btn_clear = Button(cal,padx=15,pady=6,bd=8,fg="black",font=('arial',20,'bold'),text='C',command=btnClearDisp).grid(row=5,column=2)

btn_equal = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='=',command=btnEqualsInput).grid(row=4,column=2)

division = Button(cal,padx=15,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='/',command=lambda:btnClick("/")).grid(row=4,column=3)



dot = Button(cal,padx=20,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text='.',command=lambda:btnClick('.')).grid(row=4,column=1)

remove = Button(cal,padx=15,pady=6,bd=8,fg="black",font=('arial',20,'bold'),text='X',command=RemoveLast).grid(row=5,column=3)

SINMATH = Button(cal,padx=5,pady=7,bd=8,fg="black",font=('arial',20,'bold'),text='sin',command=SinF).grid(row=5,column=0)

COSMATH = Button(cal,padx=3,pady=7,bd=8,fg="black",font=('arial',20,'bold'),text='cos',command=CosF).grid(row=5,column=1)

cal.mainloop()
