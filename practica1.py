from tkinter import *

raiz=Tk()
raiz.iconbitmap("imagenes/icono.ico")
raiz.title("calculadora")

miframe=Frame(raiz)
miframe.pack()

total=0
signo=""
number1=0
separador=0

#-----------funcion de teclado--------------
def dgitar(num):
    global separador
    if type(num) is int:
        print(numerodepantalla.get())
        if numerodepantalla.get() == '0':
            print("es cero")
            numerodepantalla.set("")
        else:
            if separador == 1:
                print("se separo cadena")
                numerodepantalla.set("")
        numerodepantalla.set(numerodepantalla.get() + str(num))
    else:
        if not '.' in numerodepantalla.get() and numerodepantalla.get() != 0:
            numerodepantalla.set(numerodepantalla.get() + num)

#-------- ver tipo de operacion
def tipo_operacion(sig):
    global signo
    global separador
    global number1
    print("number:" + str(number1))
    if number1 == 0:
        signo = sig
        separador = 1
        number1=int(numerodepantalla.get())
    else:
        total()

#--------operacion total----------
def total():
    global signo
    global number1
    global total
    print("signo: " + signo)
    if signo == "+":
        total= number1 + int(numerodepantalla.get())
        numerodepantalla.set(total)
        print("suma")
    elif signo == "-":
        total= number1 - int(numerodepantalla.get())
        print("resta")
    elif signo == "*":
        total= number1 * int(numerodepantalla.get())
        print("multiplicacion")
    elif signo == "/":
        total= number1 / int(numerodepantalla.get())
        print("division")
    else:
        print("default thing")
    numerodepantalla.set(total)
    number1 = 0

#-----------codigo de pantalla--------------
numerodepantalla=StringVar()
numerodepantalla.set(0)
pantalla=Entry(miframe,textvariable=numerodepantalla)
pantalla.grid(row=1, column=1,columnspan=4,padx=10,pady=10)
pantalla.config(bg="black",fg="green",justify="right",font="Impact",width=40)

#---------------codigo de la fila uno-----------------
boton7=Button(miframe, text="7", width=10,command=lambda:dgitar(7))
boton7.grid(row=2,column=1)
boton8=Button(miframe, text="8", width=10,command=lambda:dgitar(8))
boton8.grid(row=2,column=2)
boton9=Button(miframe, text="9", width=10,command=lambda:dgitar(9))
boton9.grid(row=2,column=3)
botondiv=Button(miframe, text="/", width=10,command=lambda:tipo_operacion("/"))
botondiv.grid(row=2,column=4)

#---------------codigo de la fila dos-----------------
boton4=Button(miframe, text="4", width=10,command=lambda:dgitar(4))
boton4.grid(row=3,column=1)
boton5=Button(miframe, text="5", width=10,command=lambda:dgitar(5))
boton5.grid(row=3,column=2)
boton6=Button(miframe, text="6", width=10,command=lambda:dgitar(6))
boton6.grid(row=3,column=3)
botonmult=Button(miframe, text="x", width=10,command=lambda:tipo_operacion("*"))
botonmult.grid(row=3,column=4)

#---------------codigo de la fila tres-----------------
boton1=Button(miframe, text="1", width=10,command=lambda:dgitar(1))
boton1.grid(row=4,column=1)
boton2=Button(miframe, text="2", width=10,command=lambda:dgitar(2))
boton2.grid(row=4,column=2)
boton3=Button(miframe, text="3", width=10,command=lambda:dgitar(3))
boton3.grid(row=4,column=3)
botonres=Button(miframe, text="-", width=10,command=lambda:tipo_operacion("-"))
botonres.grid(row=4,column=4)

#---------------codigo de la fila tres-----------------
boton0=Button(miframe, text="0", width=10,command=lambda:dgitar(0))
boton0.grid(row=5,column=1)
botonpunto=Button(miframe, text=".", width=10,command=lambda:dgitar("."))
botonpunto.grid(row=5,column=2)
botonigual=Button(miframe, text="=", width=10,command=lambda:total())
botonigual.grid(row=5,column=3)
botonsuma=Button(miframe, text="+", width=10,command=lambda:tipo_operacion("+"))
botonsuma.grid(row=5,column=4)

raiz.mainloop()