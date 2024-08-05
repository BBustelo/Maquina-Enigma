from customtkinter import *
from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor
from Teclado import Teclado
from Enigma import Enigma

teclado = Teclado()
plugboard = Plugboard()
reflectorA = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', muesca='Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', muesca='E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', muesca='V')

enigma = Enigma(reflectorA, I, II, III, plugboard, teclado)


def configurarEnigma():
    global enigma
    global I
    global II
    global III
    global plugboard

    if eleccionI.get() == 'Rotor I':
        I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', muesca='Q', inicio=inicioR1.get())
    elif eleccionI.get() == 'Rotor II':
        I = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', muesca='E', inicio=inicioR1.get())
    elif eleccionI.get() == 'Rotor III':
        I = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', muesca='V', inicio=inicioR1.get())

    if eleccionII.get() == 'Rotor I':
        II = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', muesca='Q', inicio=inicioR2.get())
    elif eleccionII.get() == 'Rotor II':
        II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', muesca='E', inicio=inicioR2.get())
    elif eleccionII.get() == 'Rotor III':
        II = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', muesca='V', inicio=inicioR2.get())

    if eleccionIII.get() == 'Rotor I':
        III = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', muesca='Q', inicio=inicioR3.get())
    elif eleccionIII.get() == 'Rotor II':
        III = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', muesca='E', inicio=inicioR3.get())
    elif eleccionIII.get() == 'Rotor III':
        III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', muesca='V', inicio=inicioR3.get())

    splitPlugboard = entradaPlugboard.get().upper().split()
    plugboard = Plugboard(splitPlugboard)

    I.setInicio(inicioR1.get())
    II.setInicio(inicioR2.get())
    III.setInicio(inicioR3.get())

    enigma = Enigma(reflectorA, I, II, III, plugboard, teclado)


def encriptar():
    texto = entradaTexto.get().upper()
    encriptado = enigma.encriptar(texto)
    salidaTexto.delete(0, 'end')
    salidaTexto.insert(0, encriptado)
    inicioR1.set(I.getDerecha()[0])
    inicioR2.set(II.getDerecha()[0])
    inicioR3.set(III.getDerecha()[0])
    print("Derecha R3: " + enigma.rotorIII.derecha)
    print("Izquierda R3: " + enigma.rotorIII.izquierda)
    print("Derecha R2: " + enigma.rotorII.derecha)
    print("Izquierda R2: " + enigma.rotorII.izquierda)
    print("Derecha R1: " + enigma.rotorI.derecha)
    print("Izquierda R1: " + enigma.rotorI.izquierda)
    print("Plugboard: " + enigma.plugboard.derecha)


app = CTk()
app.title("Maquina Enigma")
set_appearance_mode('dark')
app.geometry("1300x800")


#app.grid_columnconfigure(0, weight=3)
#app.grid_columnconfigure(1, weight=3)
#app.grid_rowconfigure(0, weight=0)
#app.grid_rowconfigure(1, weight=1)

configurarRotoresFrame = CTkFrame(master=app, border_width=2, width=400, height=200)
configurarRotoresFrame.grid(row=0, column=0, padx=20, pady=50, columnspan=2)

#configurarRotoresFrame.grid_rowconfigure(1, weight=2)
#configurarRotoresFrame.grid_rowconfigure(2, weight=2)

rotoresFrame = CTkFrame(master=configurarRotoresFrame, border_width=2)
rotoresFrame.grid(row=0, column=0, padx=10, pady=50)


label1 = CTkLabel(master=rotoresFrame, text='Configuración de rotores')
label1.grid(row=0, column=5, padx=20, pady=10)
r1Text = CTkLabel(master=rotoresFrame, text='R1')
r1Text.grid(row=1, column=3, padx=10, pady=5)
r2Text = CTkLabel(master=rotoresFrame, text='R2')
r2Text.grid(row=2, column=3, padx=10, pady=5)
r3Text = CTkLabel(master=rotoresFrame, text='R3')
r3Text.grid(row=3, column=3, padx=10, pady=5)

eleccionI = StringVar()
eleccionII = StringVar()
eleccionIII = StringVar()
opcionesRotores = ['Rotor I', 'Rotor II', 'Rotor III']
desplegableRotorI = CTkComboBox(master=rotoresFrame, values=opcionesRotores, variable=eleccionI)
desplegableRotorI.set('Rotor I')
desplegableRotorI.grid(row=1, column=5, padx=10, pady=15)
desplegableRotorII = CTkComboBox(master=rotoresFrame, values=opcionesRotores, variable=eleccionII)
desplegableRotorII.set('Rotor II')
desplegableRotorII.grid(row=2, column=5, padx=10, pady=15)
desplegableRotorIII = CTkComboBox(master=rotoresFrame, values=opcionesRotores, variable=eleccionIII)
desplegableRotorIII.set('Rotor III')
desplegableRotorIII.grid(row=3, column=5, padx=10, pady=15)

inicioRotoresFrame = CTkFrame(master=configurarRotoresFrame, border_width=2)
inicioRotoresFrame.grid(row=0, column=1, padx=10, pady=50)
label2 = CTkLabel(master=inicioRotoresFrame, text='Inicio de rotores')
label2.grid(row=0, column=5, padx=20, pady=10)
r1InicioText = CTkLabel(master=inicioRotoresFrame, text='R1')
r1InicioText.grid(row=1, column=3, padx=10, pady=15)
r2InicioText = CTkLabel(master=inicioRotoresFrame, text='R2')
r2InicioText.grid(row=2, column=3, padx=10, pady=15)
r3InicioText = CTkLabel(master=inicioRotoresFrame, text='R3')
r3InicioText.grid(row=3, column=3, padx=10, pady=15)

opcionesAlfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
inicioR1 = StringVar()
inicioR1.set(opcionesAlfabeto[0])
elegirInicioRotorI = CTkComboBox(master=inicioRotoresFrame, values=opcionesAlfabeto, variable=inicioR1)
elegirInicioRotorI.grid(row=1, column=5, padx=10, pady=15)
elegirInicioRotorI.set(opcionesAlfabeto[0])

inicioR2 = StringVar()
inicioR2.set(opcionesAlfabeto[0])
elegirInicioRotorII = CTkComboBox(master=inicioRotoresFrame, values=opcionesAlfabeto, variable=inicioR2)
elegirInicioRotorII.grid(row=2, column=5, padx=10, pady=15)
elegirInicioRotorII.set(opcionesAlfabeto[0])

inicioR3 = StringVar()
inicioR3.set(opcionesAlfabeto[0])
elegirInicioRotorIII = CTkComboBox(master=inicioRotoresFrame, values=opcionesAlfabeto, variable=inicioR3)
elegirInicioRotorIII.grid(row=3, column=5, padx=10, pady=15)
elegirInicioRotorIII.set(opcionesAlfabeto[0])

entradaPlugboard = CTkEntry(master=configurarRotoresFrame, border_width=2,
                            placeholder_text='Configurar Plugboard. Ej: ab nt kj', text_color='white', width=400, height=50)
entradaPlugboard.grid(row=1, column=0, padx=10, pady=15, sticky='ew', columnspan=2)

botonActualizar = CTkButton(configurarRotoresFrame, text='Actualizar configuracion', command=configurarEnigma)
botonActualizar.grid(row=2, padx=10, pady=10, sticky='ew', columnspan=2)

encriptarFrame = CTkFrame(app, border_width=2, width=400, height=200)
encriptarFrame.grid(row=0, column=3, padx=200, pady=50)

entradaTexto = CTkEntry(master=encriptarFrame, placeholder_text='Ingrese el texto a encriptar',
                        text_color='white', width=300, height=20)
entradaTexto.grid(row=2, column=1, padx=50, pady=15, sticky='ew', columnspan=2)
encripText = CTkLabel(master=encriptarFrame, text='Texto a encriptar: ')
encripText.grid(row=2, column=0, padx=10, pady=5)

salidaTexto = CTkEntry(master=encriptarFrame, placeholder_text='Texto encriptado',
                       text_color='white', width=300, height=20)
salidaTexto.grid(row=3, column=1, padx=50, pady=15, sticky='ew', columnspan=2)
desencripText = CTkLabel(master=encriptarFrame, text='Texto encriptado: ')
desencripText.grid(row=3, column=0, padx=10, pady=5)

botonEncriptar = CTkButton(master=encriptarFrame, text='Encriptar', command=encriptar)
botonEncriptar.grid(row=4, column=1, padx=50, pady=50, sticky='s', columnspan=2)

app.mainloop()
