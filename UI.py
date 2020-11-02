from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Code.Controller import Controller
from datetime import datetime

## Welcome to the Automatador
# Por Juan Cardona Y Roy Maestre
# 2020 - 1 Teoria de Lenguajes
# Vale por bono para el parcial

dt_string = datetime.now().strftime("_%d_%m_%Y_%H_%M_%S")
reg = open('./reg/reg'+str(dt_string)+'.txt', 'w')


def browseFile():
    try:
        global reg
        global filename
        filename = filedialog.askopenfilename(
            initialdir="./Windows", title="Seleccione un archivo", filetypes=(("Text files", "*.java*"), ("all files", "*.*")))
        global text
        mensaje.configure(text="Archivo Seleccionado: "+filename)
        text = list(open(filename, 'r'))
        text = [i.replace('\n', '')for i in text]
        lbox.delete(0, 'end')
        for i in range(len(text)):
            lbox.insert(i+1, str(i+1)+'  '+text[i])

    except:
        messagebox.showinfo("Error", "No selecciono ningun archivo")


def analizador():
    try:
        text
        global text2
        global text3

        text2 = ''
        text3 = ''
        contador = 0
        for line in text:
            controlador = Controller()
            controlador.reconocedor(line)
            for nodo in controlador.lecturas:
                text2 += "[" + str(nodo.clase) + " | " + \
                    str(nodo.valor) + " ] "
            text2 += "\n"
            evaluacion = controlador.evaluador()
            if evaluacion[0]:
                textico = ''
                for i in range(evaluacion[0]):
                    nodo = controlador.lecturas[i]
                    textico += nodo.valor + " "
                textico += "\n"
                for i in range(len(textico)):
                    textico += " "
                else:
                    textico += "^ ERROR: "
                text3 += textico
                text3 += evaluacion[1] + "\n"
            contador += 1

        text2 = text2.split('\n')
        lbox2.delete(0, 'end')

        for i in range(len(text2)):
            lbox2.insert(i+1, str(i+1)+'  '+text2[i])
            reg.write(str(i+1)+'  '+text2[i]+'\n')
        text3 = text3.split('\n')
        reg.write('\n')
        lbox3.delete(0, 'end')

        for i in range(len(text3)):
            lbox3.insert(i+1, '  '+text3[i])
            reg.write(str(i+1)+'  '+text3[i]+'\n')
        reg.write('\n')

    except:
        messagebox.showinfo("Error", "No selecciono ningun archivo")


def getReg():
    try:
        text3
        messagebox.showinfo(
            "Registro", "El registro se encuentra en la ruta: ./reg/reg"+str(dt_string)+'.txt')
        reg.close()
        ventana.destroy()
    except:
        messagebox.showinfo("Error", "No ha iniciado automatador")


# Ventana
ventana = Tk()
ventana.title('Automatador')
ventana.config(background="#353535")

# Entrada de texto
mensaje = Label(ventana, text="Seleccione un archivo *.java", fg="blue")
# posicion Etrada de texto
mensaje.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones
boton_archivo = Button(ventana, text='Escoger un archivo',
                       width=15, height=2, command=browseFile)
boton_proceso = Button(ventana, text='Iniciar automata',
                       width=15, height=2, command=analizador)
boton_reg = Button(ventana, text='Generar registro y salir',
                   width=18, height=2, command=getReg)

# Posición de botones
boton_archivo.grid(row=1, column=0, padx=7, pady=5)
boton_proceso.grid(row=1, column=1, padx=5, pady=5)
boton_reg.grid(row=1, column=2, padx=5, pady=5)

# Cajor que muestra
lbox = Listbox(ventana, height=11, width=80)
lbox2 = Listbox(ventana, height=13, width=180)
lbox3 = Listbox(ventana, height=13, width=180)

# Posición de cajon
lbox.grid(row=2, column=1)
lbox2.grid(row=3, column=0, columnspan=3)
lbox3.grid(row=4, column=0, columnspan=3)

ventana.mainloop()
