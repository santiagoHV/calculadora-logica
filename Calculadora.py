import tkinter as tk
import cadena
import ttg
import os


class VentanaCalculadora(tk.Tk):

    def __init__(self):
        super(VentanaCalculadora, self).__init__()
        self.title("Calculadora Logica")
        self.geometry('450x320')
        self.config(bd=15)
        self.config(background="#FFF057")
        self.resizable(False, False)
        self.entrada = tk.StringVar()

        self.pantalla = tk.Entry(
            self,
            font=("Arial", 14),
            background="#000000",
            fg='#FFFFFF',
            borderwidth=5,
            width=35,
            textvariable=self.entrada
        )
        self.pantalla.grid(row=0, column=0, columnspan=4,  pady=25)

        btnP = tk.Button(self, text='p', command=lambda: self.escribir('p'))
        self.configurar_boton(btnP)
        btnP.grid(row=2, column=0, pady=5)

        btnQ = tk.Button(self, text='q', command=lambda: self.escribir('q'))
        self.configurar_boton(btnQ)
        btnQ.grid(row=2, column=1)

        btnR = tk.Button(self, text='r', command=lambda: self.escribir('r'))
        self.configurar_boton(btnR)
        btnR.grid(row=2, column=2)

        btnCondicional = tk.Button(self, text='→', command=lambda: self.escribir('→'))
        self.configurar_boton(btnCondicional)
        btnCondicional.grid(row=2, column=3)

        btnConjuncion = tk.Button(self, text='^', command=lambda: self.escribir('^'))
        self.configurar_boton(btnConjuncion)
        btnConjuncion.grid(row=3, column=0, pady=5)

        btnDisyuncion = tk.Button(self, text='v', command=lambda: self.escribir('v'))
        self.configurar_boton(btnDisyuncion)
        btnDisyuncion.grid(row=3, column=1)

        btnNegacion = tk.Button(self, text='~', command=lambda: self.escribir('~'))
        self.configurar_boton(btnNegacion)
        btnNegacion.grid(row=3, column=2)

        btnBicondicional = tk.Button(self, text='↔', command=lambda: self.escribir('↔'))
        self.configurar_boton(btnBicondicional)
        btnBicondicional.grid(row=3, column=3)

        btnIgual = tk.Button(self, text='=', command=self.mostrar_resultado)
        self.configurar_boton(btnIgual)
        btnIgual.grid(row=4, column=2, pady=5)

        btnBorrar = tk.Button(self, text='AC', command=self.limpiar)
        self.configurar_boton(btnBorrar)
        btnBorrar.grid(row=4, column=3)

        btnParentesisA = tk.Button(self, text='(', command=lambda: self.escribir('('))
        self.configurar_boton(btnParentesisA)
        btnParentesisA.grid(row=4, column=0)

        btnParentesisC = tk.Button(self, text=')', command=lambda: self.escribir(')'))
        self.configurar_boton(btnParentesisC)
        btnParentesisC.grid(row=4, column=1)

        btnParentesisB = tk.Button(self, text='[', command=lambda: self.escribir('['))
        self.configurar_boton(btnParentesisB)
        btnParentesisB.grid(row=5, column=0, pady= 5)

        btnParentesisD = tk.Button(self, text=']', command=lambda: self.escribir(']'))
        self.configurar_boton(btnParentesisD)
        btnParentesisD.grid(row=5, column=1, pady=5)

        btnManual= tk.Button(self, text='Instrucciones', command=self.manual)
        self.configurar_boton(btnManual)
        btnManual.grid(row=5, column=2, columnspan = 2)
        btnManual.config(width = 15)

        self.mainloop()

    def escribir(self, caracter):
        self.pantalla.insert(self.pantalla.index(tk.INSERT), caracter)
        os.system('cls')

    def limpiar(self):
        self.pantalla.delete(0, 'end')
        os.system('cls')

    def manual(self):
        print ("CALCULADORA LOGICA"+'\n'+'\n'+
              "Los parentesis '[' y ']'  funcionan para encerrar otras proposiciones,"+'\n' +
              "el uso correcto de dichos parentesis radica en usarlos para los extremos"+'\n' +
              "EJEMPLO:"+'\n' +
              "[(pvq)=>r] => q" +'\n'+'\n'+
              "Las variables logicas corresponden a:"+'\n'+"'p', 'q' y 'r'"+'\n'+'\n'+
              "Los operadores logicos corresponden a "+'\n'+ "'^', 'v', '→' y '↔'"+'\n'+
              "respectivamente corresponden a"+'\n'+"'and', 'or', 'si, entonces' y 'si, y solo si'"+'\n'+'\n'+
              "Con 'AC' limpia la pantalla"+'\n'+"Con '=' brinda la tabla de verdad en consola"+'\n')

    def mostrar_resultado(self):
        try:
            aux = cadena.proposicion(self.entrada.get())
            var = cadena.variables(self.entrada.get())

            prep = cadena.preposicionesConjugadas(self.entrada.get())
            list(aux)
            prep.append(aux)

            table = ttg.Truths(var,[aux])
            table2 = ttg.Truths(var,prep)
            print(aux)
            print(table2)
            print(table.valuation())
        except BaseException:
            print('Entrada invalida')

    def configurar_boton(self, boton):
        boton.config(
            font=('Arial', 12, 'bold'),
            bg='#000000',
            width=5,
            height=1,
            fg='#cae8d5',
            padx=7,
            pady=4
        )


main = VentanaCalculadora()
